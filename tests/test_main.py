import unittest
from src.main import main

class TestMain(unittest.TestCase):
    def test_main_runs(self):
        # Apenas testa se a função principal executa sem erros
        try:
            main()
        except Exception as e:
            self.fail(f"main() levantou uma exceção: {e}")

if __name__ == "__main__":
    unittest.main()