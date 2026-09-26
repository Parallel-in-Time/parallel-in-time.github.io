import unittest

from utils import parseArxivPage


class ParseArxivPageTests(unittest.TestCase):
    def test_parse_arxiv_page_extracts_metadata(self):
        html = """
        <html>
          <head>
            <meta name="citation_title" content="A parallel-in-time paper" />
            <meta name="citation_author" content="Jane Doe" />
            <meta name="citation_author" content="John Smith" />
            <meta name="citation_date" content="2026/09/30" />
            <meta name="citation_abstract" content="  An abstract with   extra spacing. " />
            <meta name="citation_abstract_html_url" content="https://arxiv.org/abs/2609.24434" />
            <meta name="citation_keywords" content="Numerical Analysis (math.NA); Analysis of PDEs (math.AP)" />
          </head>
        </html>
        """

        entry = parseArxivPage(html, "https://arxiv.org/abs/2609.24434", "2609.24434")

        self.assertEqual(entry["title"], "A parallel-in-time paper")
        self.assertEqual(entry["published"], "2026-09-30")
        self.assertEqual(entry["summary"], "An abstract with extra spacing.")
        self.assertEqual(entry["link"], "https://arxiv.org/abs/2609.24434")
        self.assertEqual(entry["id"], "https://arxiv.org/abs/2609.24434")
        self.assertEqual(entry["arxiv_primary_category"]["term"], "math.NA")
        self.assertEqual(
            entry["authors"],
            [{"name": "Jane Doe"}, {"name": "John Smith"}],
        )


if __name__ == "__main__":
    unittest.main()
