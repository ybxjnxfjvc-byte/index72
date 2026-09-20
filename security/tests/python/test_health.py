import unittest,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'lab'))
from health_service import payload
class T(unittest.TestCase):
 def test_health(self): self.assertEqual(payload('/health'),(200,{'ok':True,'service':'portfolio-security-lab'}))
 def test_404(self): self.assertEqual(payload('/x')[0],404)
if __name__=='__main__':unittest.main()
