from main import validate


def test_validate():

    @validate(0, 256)
    def set_pixel(red: int, green: int, blue: int) -> str:
        return "Pixel created!"

    assert set_pixel(0, 127, 300) == "Function call is not valid!"
    assert set_pixel(0, 127, 250) == "Pixel created!"


if __name__ == "__main__":
    test_validate()
