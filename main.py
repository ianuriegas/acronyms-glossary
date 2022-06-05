from fpdf import FPDF

# reads text file and stores info into an empty list
def read_txt():
    with open('glossary.txt', 'r') as txt_file:
        lines_list = []
        # read in all lines of text file
        for line in txt_file:
            stripped_line = line.strip()
            lines_list.append(stripped_line)

    return lines_list


# sorts new list using insertion sort
def insertion_sort(lines_list):
    indexing_length = range(1,len(lines_list))
    for i in indexing_length:
        value = lines_list[i]

        while value < lines_list[i-1] and i>0:
            lines_list[i],lines_list[i-1]=lines_list[i-1],lines_list[i]
            i=i-1

    return lines_list


# writes new list back into existing text file
def write_txt(sorted_list):
    with open('glossary.txt', 'w') as txt_file:
        for element in sorted_list:
            txt_file.write(element + "\n")


def sort_acronym(acronym_to_sort):
    # reads in text file and stores it in empty list
    # also adds acronym that needs to be added at the end of the empty list
    lines_list = read_txt()
    lines_list.append(acronym_to_sort)

    # insertion sort function sorts the empty list
    sorted_list = insertion_sort(lines_list)

    # write the new list to the text file
    write_txt(sorted_list)


def export_pdf():
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # set style and size of font
    # that you want in the pdf

    with open('glossary.txt', 'r') as txt_file:
        pdf.set_font("Arial", size=15)
        # insert the texts in pdf
        for x in txt_file:
            pdf.cell(200, 10, txt=x, ln=1, align='C')

        # save the pdf with name .pdf
        pdf.output("glossary.pdf")


def main():
    while True:
        # takes acronym that needs sorting
        acronym_to_sort = input('Enter using format: "ACRONYM - DEFINITION", or type "QUIT" to leave: ')

        # we need everything to be uppercase, if acronym isn't uppercase, make it uppercase
        if not acronym_to_sort.isupper():
            acronym_to_sort = acronym_to_sort.upper()

        # quit breaks the program
        if acronym_to_sort == "QUIT":
            print("Goodbye")
            break;

        if "-" not in acronym_to_sort:
            print("Wrong format idiot, can you read?")
            break;
        else:
            # sorts acronym
            sort_acronym(acronym_to_sort)
            export_pdf()


if __name__ == "__main__":
    main()