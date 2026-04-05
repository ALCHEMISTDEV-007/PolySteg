import random
from datetime import datetime, timedelta
import piexif

class MetadataSpoofer:
    @staticmethod
    def _generate_fake_date():
        """Generates a random datetime in the past 1 to 5 years."""
        days_ago = random.randint(365, 365 * 5)
        fake_date = datetime.now() - timedelta(days=days_ago)
        return fake_date

    @staticmethod
    def get_image_exif(spoof_hint: str) -> bytes:
        """
        Generates realistic piexif byte data based on a spoof hint.
        Example: spoof_hint = "Canon EOS 5D"
        """
        fake_date = MetadataSpoofer._generate_fake_date()
        date_str = fake_date.strftime("%Y:%m:%d %H:%M:%S")
        
        # Parse hint. Ex: "Canon EOS 5D", fallback to generic "FakeMake"
        parts = spoof_hint.split(" ", 1)
        make = parts[0] if parts else "Generic"
        model = spoof_hint
        
        software = "Adobe Photoshop CC 2019 (Windows)"

        exif_dict = {
            "0th": {
                piexif.ImageIFD.Make: make.encode('utf-8'),
                piexif.ImageIFD.Model: model.encode('utf-8'),
                piexif.ImageIFD.Software: software.encode('utf-8'),
                piexif.ImageIFD.DateTime: date_str.encode('utf-8')
            },
            "Exif": {
                piexif.ExifIFD.DateTimeOriginal: date_str.encode('utf-8'),
                piexif.ExifIFD.DateTimeDigitized: date_str.encode('utf-8'),
                # Faking realistic lens properties
                piexif.ExifIFD.FocalLength: (50, 1),
                piexif.ExifIFD.ISOSpeedRatings: 100,
            }
        }
        
        return piexif.dump(exif_dict)

    @staticmethod
    def get_pdf_info(spoof_hint: str) -> dict:
        """
        Generates realistic PDF Document Info.
        """
        fake_date = MetadataSpoofer._generate_fake_date()
        # PDF date format: D:YYYYMMDDHHmmSSZ
        pdf_date = f"D:{fake_date.strftime('%Y%m%d%H%M%S')}Z"
        
        return {
            '/Author': spoof_hint,
            '/Creator': 'Microsoft® Word for Office 365',
            '/Producer': 'macOS Version 10.14.6 (Build 18G103) Quartz PDFContext',
            '/CreationDate': pdf_date,
            '/ModDate': pdf_date
        }
