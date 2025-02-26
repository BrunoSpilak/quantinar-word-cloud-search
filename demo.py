from quantinar_world_cloud_search.parser import converter_pdf_json_count

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description='Convert a PDF file to a JSON Metadata containing the '
                    'word counts.')
    parser.add_argument('path', help='The path of the pdf you want to convert')
    parser.add_argument('-o', '--output',
                        help='The type of output you wish to have. Can be '
                             'console or file. For file output you should '
                             'also add filename argument')
    parser.add_argument('-f', '--filename',
                        help='The name of the file you want the output to.')

    args = parser.parse_args()

    if args.output == 'console':
        print(converter_pdf_json_count(args.path, file_name=""))
    elif args.output == 'file':
        if args.filename is None or args.filename == "":
            raise parser.error(
                '--path argument is required when output type is file')
        converter_pdf_json_count(args.path, file_name=args.filename)
