"""Pruebas de los contratos de presentación exigidos por la rúbrica."""

from html.parser import HTMLParser
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
CSS = (ROOT / "assets/css/styles.css").read_text(encoding="utf-8")


class ImageAndLinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []
        self.links = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if data.get("id"):
            self.ids.add(data["id"])
        if tag == "img":
            self.images.append(data)
        if tag == "a":
            self.links.append(data)


class SiteRubricTests(unittest.TestCase):
    def test_process_steps_are_a_semantic_ordered_list(self):
        """Quitar el ol o cualquiera de los li debe romper el contrato de estructura HTML."""
        process = re.search(r'<section\b[^>]*\bid="proceso"[^>]*>(.*?)</section>', HTML, re.S)
        self.assertIsNotNone(process)
        tags = re.findall(r'<(/?)(ol|li)\b[^>]*>', process.group(1))
        self.assertEqual(tags.count(("", "ol")), 1)
        self.assertEqual(tags.count(("", "li")), 3)
        self.assertEqual(tags.count(("/", "li")), 3)
        self.assertEqual(tags.count(("/", "ol")), 1)

    def test_intro_has_single_column_layout_for_narrow_tablets(self):
        """La regresión de 601 px con columna fija de 320 px falla sin este ajuste."""
        query = re.search(r'@media\s*\(min-width:\s*601px\)\s*and\s*\(max-width:\s*800px\)\s*\{(.{0,220})', CSS, re.S)
        self.assertIsNotNone(query)
        self.assertRegex(query.group(1), r'\.intro\s*\{\s*display:\s*block')

    def test_site_requests_fresh_css_after_publication(self):
        """Una caché antigua de GitHub Pages no debe impedir aplicar el CSS nuevo."""
        self.assertRegex(HTML, r'href="assets/css/styles\.css\?v=[0-9a-zA-Z_-]+"')

    def test_visible_images_use_real_assets_and_alt_text(self):
        """Una referencia a imagen inexistente o sin descripción debe fallar."""
        parser = ImageAndLinkParser()
        parser.feed(HTML)
        self.assertGreaterEqual(len(parser.images), 15)
        for image in parser.images:
            with self.subTest(source=image.get("src")):
                self.assertTrue(image.get("alt", "").strip())
                self.assertTrue((ROOT / image["src"]).is_file())
        for anchor in parser.links:
            href = anchor.get("href", "")
            if href.startswith("#"):
                self.assertIn(href[1:], parser.ids)

    def test_story_images_fit_a_mobile_transfer_budget(self):
        """Volver a imágenes de ~2 MB por escena debe activar la prueba."""
        images = list((ROOT / "assets/images/martes").glob("escena-*.webp"))
        self.assertEqual(len(images), 12)
        self.assertLessEqual(sum(image.stat().st_size for image in images), 7_000_000)
        for image in images:
            with self.subTest(image=image.name):
                self.assertLessEqual(image.stat().st_size, 750_000)

    def test_hero_and_brand_have_lightweight_webp_assets(self):
        """Las imágenes pesadas del primer pantallazo no deben volver a servirse."""
        hero = ROOT / "assets/images/hero-capricornio.webp"
        brand = ROOT / "assets/images/logo-capricornio-legible.webp"
        self.assertTrue(hero.is_file())
        self.assertTrue(brand.is_file())
        self.assertLessEqual(hero.stat().st_size, 750_000)
        self.assertLessEqual(brand.stat().st_size, 750_000)
        self.assertIn("assets/images/hero-capricornio.webp", HTML)
        self.assertIn("assets/images/logo-capricornio-legible.webp", HTML)
        self.assertIn("hero-capricornio.webp", CSS)


if __name__ == "__main__":
    unittest.main()
