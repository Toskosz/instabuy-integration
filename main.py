


def main():
    API.load_config()

    p_int = ProductIntegration()
    p_int.update("path", 500)
    p_int.create("path_create", 200)
    p_int.delete("path_delete", 300)


if __name__ == '__main__':
    main()
