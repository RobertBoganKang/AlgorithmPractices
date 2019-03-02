import argparse
import glob
import os


def get_title(path_table):
    # get titles for one file
    with open(path_table, 'r') as f:
        t = f.readline().strip()
        line = t.split(',')
        return line


def get_titles(tables):
    """
    :param tables: list(str); paths of tables
    :return:
    """
    s = []
    for i in range(len(tables)):
        s.extend(get_title(tables[i]))
    s = list(set(s))
    s.sort()
    return s


def get_index(tables):
    title = get_titles(tables)
    tables_index_array = []
    for t in tables:
        table_title = get_title(t)
        index_array = []
        for tt in title:
            if tt in table_title:
                index_array.append(table_title.index(tt))
            else:
                index_array.append(None)
        tables_index_array.append(index_array)
    return tables_index_array


def combine_table_main(tables, out_path):
    # get all titles
    titles = get_titles(tables)
    # get index array as export rule for all tables
    index_array = get_index(tables)
    # write out files
    with open(out_path, 'w+') as out:
        # write titles
        out.write(','.join(titles))
        out.write('\n')
        # loop all tables
        for i in range(len(tables)):
            # read tables
            with open(tables[i], 'r') as t:
                # jump first line
                t.readline()
                # export lines to the out_path file
                while 1:
                    # read lines
                    line = t.readline()
                    # line end sign
                    if not line:
                        break
                    # get lines
                    line = line.strip().split(',')
                    # make lines to export
                    manipulated_line = []
                    for j in range(len(index_array[0])):
                        if index_array[i][j] is not None:
                            manipulated_line.append(line[index_array[i][j]])
                        else:
                            manipulated_line.append('Null')
                    manipulated_line = ','.join(manipulated_line)
                    out.write(manipulated_line)
                    out.write('\n')


def get_csv(folder):
    """
    get input path of csv
    :param folder:
    :return:
    """
    fs = glob.glob(os.path.join(folder, '**/*.csv'), recursive=True)
    return fs


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='join tables')
    parser.add_argument('--input', '-i', type=str, help='input folder contains many tables', default='in')
    parser.add_argument('--output', '-o', type=str, help='out csv', default='out.csv')
    args = parser.parse_args()

    combine_table_main(get_csv(args.input), args.output)
