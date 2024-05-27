from unittest import TestCase
from swf_firewall.swf_utils import NO_COMPRESSION_SWF_SIGNATURE
from swf_firewall.swf_utils import LZMA_COMPRESSION_SWF_SIGNATURE
from swf_firewall.swf_utils import ZLIB_COMPRESSION_SWF_SIGNATURE


class TestSignatureConstants(TestCase):
	# for information on signatures, see: https://open-flash.github.io/mirrors/swf-spec-19.pdf#page=27
	def test_no_compression_swf_signature_constant_should_be_uppercase_fws_bytes(self):
		# the signature for a SWF that doesn't use compression is FWS.
		self.assertEqual(b"FWS", NO_COMPRESSION_SWF_SIGNATURE)

	def test_zlib_compression_swf_signature_constant_should_be_uppercase_cws_bytes(self):
		# the signature for a SWF that uses ZLIB compression is CWS
		self.assertEqual(b"CWS", ZLIB_COMPRESSION_SWF_SIGNATURE)

	def test_lzma_compression_swf_signature_constant_should_be_uppercase_zws_bytes(self):
		# the signature for a SWF that uses LZMA compression is ZWS
		self.assertEqual(b"ZWS", LZMA_COMPRESSION_SWF_SIGNATURE)
