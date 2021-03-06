import os
import platform
import re
import logging
import pandas as pd
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
# All ERROR and below events would be discarded
logging.disable(logging.DEBUG)
# Define basic configuration for the logging system
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')
logging.info('start of the program')

# Define a dictionary of SAS procedure, SAS product and procedure category
def init_proc_cat_prod(cat_prod_dict):
    # get current path
    current_path = os.getcwd()
    if platform.system() == 'Windows':
        wrk_cat_ref_df = pd.read_csv(current_path+'\\reference\\' + 'D_CLDASST_DISC_WRK_CAT_REF.csv')
    else:
        wrk_cat_ref_df = pd.read_csv(current_path+'/reference/' + 'D_CLDASST_DISC_WRK_CAT_REF.csv')

    wrk_cat_ref_df = wrk_cat_ref_df[['SAS9_Proc', 'SAS9_Prod', 'SAS9_Proc_Cat']]

    #  iterate over wrk_cat_ref_df， return a dictionary: cat_prod_dict
    for index, row in wrk_cat_ref_df.iterrows():
        key = row['SAS9_Proc']
        sas9_prod = row['SAS9_Prod']
        sas9_proc_cat = row['SAS9_Proc_Cat']
        cat_prod_dict[key] = (sas9_prod, sas9_proc_cat)

    return cat_prod_dict


# Define a dictionary of migration rule
def init_migr_rule():
    migr_rule_dict = dict()
    current_path = os.getcwd()
    if platform.system() == 'Windows':
        migr_rule_ref_df = pd.read_csv(current_path + '\\reference\\' + 'D_CLDASST_DISC_MIGR_RULE_REF.csv')
    else:
        migr_rule_ref_df = pd.read_csv(current_path + '/reference/' + 'D_CLDASST_DISC_MIGR_RULE_REF.csv')

    for index, row in migr_rule_ref_df.iterrows():
        key = str(row['ID'])
        migr_rule = row['RULE']
        migr_rule_dict[key] = migr_rule

    return migr_rule_dict


# Define a tuple for in-memory flag
def init_inmem():
    inmem_list = []
    current_path = os.getcwd()
    if platform.system() == 'Windows':
        inmem_ref_df = pd.read_csv(current_path + '\\reference\\' + 'D_CLDASST_DISC_INMEM_FLG_REF.csv')
    else:
        inmem_ref_df = pd.read_csv(current_path + '/reference/' + 'D_CLDASST_DISC_INMEM_FLG_REF.csv')

    for index, row in inmem_ref_df.iterrows():
        inmem_list.append(row['INMEM_KEYWORD'])

    inmem_tuple = tuple(inmem_list)

    return inmem_tuple


# Define a tuple for proc-grid flag
def init_proc_grid():
    proc_grid_list = []
    current_path = os.getcwd()
    if platform.system() == 'Windows':
        proc_grid_ref_df = pd.read_csv(current_path + '\\reference\\' + 'D_CLDASST_DISC_PROC_GRID_FLG_REF.csv')
    else:
        proc_grid_ref_df = pd.read_csv(current_path + '/reference/' + 'D_CLDASST_DISC_PROC_GRID_FLG_REF.csv')

    for index, row in proc_grid_ref_df.iterrows():
        proc_grid_list.append(row['PROC_GRID_KEYWORD'])

    proc_grid_tuple = tuple(proc_grid_list)

    return proc_grid_tuple


# Get file names in 'Adapter/logs' folder in a recursive way
def getInventory(current_path, current_folder, visited, file_list):
    if platform.system() == 'Windows':
        current_path = current_path + '\\' + current_folder
    else:
        current_path = current_path + '/' + current_folder

    visited[current_path] = True
    logging.debug("current path is " + current_path)
    folders = []
    current_path_files = os.listdir(current_path)
    for file_or_folder in current_path_files:

        if platform.system() == 'Windows':
            pointedPath = current_path + '\\' + file_or_folder
        else:
            pointedPath = current_path + '/' + file_or_folder
        if os.path.isdir(pointedPath):
            folders.append(file_or_folder)
        else:
            file_list.append((current_path, file_or_folder))

    logging.debug("file list is")
    for filepath, filename in file_list:
        logging.debug(filepath + " " + filename)
    logging.debug("***************************")
    for child_folder in folders:

        if platform.system() == 'Windows':
            pointedPath = current_path + '\\' + child_folder
        else:
            pointedPath = current_path + '/' + child_folder

        if visited.get(pointedPath) is None:
            logging.debug("go down to " + child_folder)
            getInventory(current_path, child_folder, visited, file_list)


# get sas file id
def get_sas_file_id(current_path, current_folder, visited, file_list):
    if platform.system() == 'Windows':
        current_path = current_path + '\\' + current_folder
    else:
        current_path = current_path + '/' + current_folder

    visited[current_path] = True
    logging.debug("current path is " + current_path)
    folders = []
    current_path_files = os.listdir(current_path)
    for file_or_folder in current_path_files:
        if platform.system() == 'Windows':
            child_path = current_path + '\\' + file_or_folder
        else:
            child_path = current_path + '/' + file_or_folder

        if os.path.isdir(child_path):
            folders.append(file_or_folder)
        else:

            file_list.append((current_path, file_or_folder))

    for child_folder in folders:

        if platform.system() == 'Windows':
            child_path = current_path + '\\' + child_folder
        else:
            child_path = current_path + '/' + child_folder

        if visited.get(child_path) is None:
            logging.debug("go down to " + child_folder)
            getInventory(current_path, child_folder, visited, file_list)

    sas_file_dict = dict()
    counter = 1
    sas_extensions = ['ddf', 'djf', 'egp', 'sas', 'sas7bcat', 'sas7bdat', 'sas7bitm', 'sc2', 'sct01', 'sd2', 'spds9',
                      'sri', 'ssd01', 'xsq']
    for path, file_name in file_list:
        extension = file_name.split('.')[1]
        if extension in sas_extensions:
            sas_file_dict[file_name] = 'SF_' + str(counter)
            counter+=1
    return sas_file_dict


# read log contents from given file_path
# return log file as a big string
# completed
def get_log_content(file_path):
    file_object = open(file_path)
    file_content = file_object.read()
    file_object.close()
    return file_content


# get all the user name of the given log file
# return a list of usernames
# comment: need to implement multi-user cases (1/14)
def get_user_name(log_content):
    user_name_regex = re.compile(r".*?].*?:(.*) - ")
    user_name_obj = user_name_regex.search(log_content[:1000])
    user_name = user_name_obj.group(1).split('@')
    return user_name[0]


# provide a user's log file content given username and log_content
# comment: need to implement split the log content based on the given user name (1/14)
def get_user_log_content(user, log_content):
    return log_content


# input data: user's log content
# split the user's log content based on SAS file
# make a list of pair of SAS file name and the SAS file's log content
# comment: need to implement SAS file line number part here (1/14)
def get_sas_files(user_log_content):
    sas_content_list = user_log_content.split("%LET _CLIENTPROJECTPATH=")

    sas_content_numbered_list = sas_line_number_counter(sas_content_list)
    sas_file_list = []

    for sas_content in sas_content_numbered_list:
        program_file_regex = re.compile(r" _SASPROGRAMFILE=(.*);")
        program_file_list = program_file_regex.findall(sas_content)

        project_path_regex = re.compile(r" _CLIENTPROJECTPATH=(.*);")
        project_path_list = project_path_regex.findall(sas_content)

        if len(program_file_list) != 0 and len(program_file_list[0]) > 3:
            sas_file_list.append(program_file_list[0][1:-1])
        elif len(project_path_list) != 0 and len(project_path_list[0]) > 3:
            sas_file_list.append(project_path_list[0][1:-1])
        else:
            sas_file_list.append("")

    zipped_sas_file_content_list = tuple(zip(sas_file_list, sas_content_numbered_list))

    return zipped_sas_file_content_list


# count SAS line number
def sas_line_number_counter(sas_content_list):
    temp_chunk = ""

    sas_content_numbered_list = []
    sas_full_content_list = []
    # recover the lost part when log file is split
    for count, content in enumerate(sas_content_list):
        if count != 0:
            content = "%LET _CLIENTPROJECTPATH=" + content
        sas_full_content_list.append(content)

    # line number counting for the first part of the sas log file (usually SAS initialization)
    for line_num, line in enumerate(sas_full_content_list[0].splitlines(True)):
        temp_chunk += str(line_num + 1) + "  " + line

    sas_content_numbered_list.append(temp_chunk)

    temp_chunk = ""
    # line number counting for the remaining parts
    for sas_content in sas_full_content_list[1:]:

        line_number_regex = re.compile(r"\n\d\d\d\d-\d\d-.* - (\d+) ")
        line_number_regex_obj = line_number_regex.search(sas_content)
        start_line_number = int(line_number_regex_obj.group(1))

        for line in sas_content.splitlines(True):
            temp_chunk += str(start_line_number - 1) + "  " + line
            start_line_number += 1
        sas_content_numbered_list.append(temp_chunk)
        temp_chunk = ""

    return sas_content_numbered_list


# get SAS file line number
def get_sas_file_line_number(record_content):
    sas_file_line_regex = re.compile(r"(.*)  \d\d\d\d-\d\d-\d\d.*\(Total process time\):")
    sas_file_line_obj = sas_file_line_regex.search(record_content)
    if sas_file_line_obj is None:
        return ""
    else:
        return float(sas_file_line_obj.group(1))


# get input file such as *.csv
# if there is not an input file, then return ""
# completed
def get_input_file_name(sas_file_content):
    input_file_name_regex = re.compile(r"NOTE: The infile \'(.*)\' is:")
    input_file_list = input_file_name_regex.findall(sas_file_content)

    input_file_dict = dict()

    for input_file in input_file_list:
        if not input_file_dict.get(input_file):
            input_file_dict[input_file] = '0'

    input_row_file_name_regex = re.compile(r"NOTE: (.*) records were read from the infile \'(.*)\'.")
    input_row_file_list = input_row_file_name_regex.findall(sas_file_content)

    for row, input_file in input_row_file_list:
        input_file_dict[input_file] = row

    rows = ''
    input_files = ''
    if len(input_file_dict) != 0:
        for input_file, row in input_file_dict.items():
            rows += ';' + row
            input_files += ';' + input_file

    return rows[1:], input_files[1:]


# get SAS Step names such as DATA statement, Procedure SQL, SAS Initialization
# return SAS STEP (such as DATA statement) and SAS Step name (ex)sql, Data
# Completed but need to check if there is any other case regarding SAS Step (1/14)
def get_sas_step_name(sas_file_content):
    sas_step_name_regex = re.compile(r"NOTE: (.*) (.*) used")
    sas_step_name_regex_obj = sas_step_name_regex.search(sas_file_content)

    if sas_step_name_regex_obj is None:
        sas_step = ''
        sas_step_name = ''
    elif sas_step_name_regex_obj.group(1) == 'DATA':
        sas_step = sas_step_name_regex_obj.group(1) + ' ' + sas_step_name_regex_obj.group(2)
        sas_step_name = sas_step_name_regex_obj.group(1)
    elif sas_step_name_regex_obj.group(1) == 'PROCEDURE':
        sas_step = 'PROCEDURE Statement'
        sas_step_name = sas_step_name_regex_obj.group(2)
    elif sas_step_name_regex_obj.group(1) == 'SAS':
        sas_step = 'SAS Initialization'
        sas_step_name = ''
    elif sas_step_name_regex_obj.group(1) == 'The SAS':
        sas_step = 'SAS System'
        sas_step_name = ''
    else:
        sas_step = ''
        sas_step_name = ''
    return sas_step, sas_step_name


# get time information
# return execution date and execution time
# completed
def get_time_info(sas_file_content):
    time_info_regex = re.compile(r"(\d\d\d\d-\d\d-\d\d)T(\d\d:\d\d:\d\d).*real time")
    time_info_regex_obj = time_info_regex.search(sas_file_content)

    if time_info_regex_obj is None:
        print("time info cannot get regex object")
        exc_date = "error"
        exc_time = "error"
    else:
        exc_date = time_info_regex_obj.group(1)
        exc_time = time_info_regex_obj.group(2)

    return exc_date, exc_time


# get process time for cpu time and real time
# return cpu time and real time as second
def get_process_time(sas_file_content):
    cpu_time_regex = re.compile(r"cpu time \s+(\d+\.\d+)")
    cpu_time_regex_obj = cpu_time_regex.search(sas_file_content)
    if cpu_time_regex_obj is None:
        cpu_time_regex = re.compile(r"cpu time \s+(\d+:\d+.\d+) ")
        cpu_time_regex_obj = cpu_time_regex.search(sas_file_content)
        cpu_time_list = cpu_time_regex_obj.split(':')
        cpu_time = float(cpu_time_list[0]) * 60 + float(cpu_time_list[1])
    else:
        cpu_time = float(cpu_time_regex_obj.group(1))

    real_time_regex = re.compile(r"real time \s+(\d+\.\d+)")
    real_time_regex_obj = real_time_regex.search(sas_file_content)
    if real_time_regex_obj is None:
        real_time_regex = re.compile(r"real time \s+(\d+:\d+.\d+) ")
        real_time_regex_obj = real_time_regex.search(sas_file_content)
        real_time_list = real_time_regex_obj.split(':')
        real_time = float(real_time_list[0]) * 60 + float(cpu_time_list[1])
    else:
        real_time = float(real_time_regex_obj.group(1))

    return cpu_time, real_time


# get output library and output table from regular log message such as NOTE: ~~
# return output library and output table
def get_output_library_table(sas_file_content):
    output_lib_table_regex_1 = re.compile(r"NOTE: The data set (.*)\.(.*) has \d+ observations and \d+ "
                                          r"variables.")
    output_lib_table_list_1 = output_lib_table_regex_1.findall(sas_file_content)

    output_lib_table_regex_2 = re.compile(r"NOTE: SQL view (.*)\.(.*) has been defined.")
    output_lib_table_list_2 = output_lib_table_regex_2.findall(sas_file_content)

    output_lib_table_regex_3 = re.compile(r"NOTE: Table (.*?)\.(.*?) created, with \d+ rows and \d+ columns.")
    output_lib_table_list_3 = output_lib_table_regex_3.findall(sas_file_content)

    output_lib_table_regex_4 = re.compile(r"NOTE: Table (.*?)\.(.*?) has been modified, with \d+ columns.")
    output_lib_table_list_4 = output_lib_table_regex_4.findall(sas_file_content)

    output_lib_table_list = output_lib_table_list_1 + output_lib_table_list_2 + output_lib_table_list_3 + \
                            output_lib_table_list_4

    output_lib = ''
    output_table = ''

    if len(output_lib_table_list) != 0:
        for idx, record in enumerate(output_lib_table_list):
            if idx == 0:
                # print(record)
                output_lib += record[0]
                output_table += record[1]
            else:
                output_lib += ';' + record[0]
                output_table += ';' + record[1]

    return output_lib, output_table


# get input library and input table from regular log output such as NOTE: ~
# return input_lib, input_table as string
def get_input_library_table(sas_file_content):
    input_lib_table_regex_case_one = re.compile(r"NOTE: There were \d+ observations read from the data set (.*)\.(.*).")
    input_lib_table_list = input_lib_table_regex_case_one.findall(sas_file_content)

    input_lib_table_regex_case_two = re.compile(r"NOTE: \d+ rows were updated in (.*)\.(.*).")
    input_lib_table_list += input_lib_table_regex_case_two.findall(sas_file_content)

    input_lib_table_regex_case_three = re.compile(r"NOTE: .*? rows were deleted from (.*)\.(.*).")
    input_lib_table_list += input_lib_table_regex_case_three.findall(sas_file_content)

    input_lib_table_regex_case_four = re.compile(r"NOTE: 1 row was updated in (.*)\.(.*).")
    input_lib_table_list += input_lib_table_regex_case_four.findall(sas_file_content)

    input_lib = ''
    input_table = ''

    seen = set()
    seen_add = seen.add
    input_lib_table_list = [x for x in input_lib_table_list if not (x in seen or seen_add(x))]

    if len(input_lib_table_list) != 0:
        for record in input_lib_table_list:
            input_lib += ';' + record[0]
            input_table += ';' + record[1]

    return input_lib[1:], input_table[1:]


# get number of rows write and output library and output table.
# got the information from three regular log output
# return a list of [rows, libs, tbls] ex) [row1;row2, lib1;lib2, table1; table2]
def get_sas_row_write(record_content):
    rows = libs = tbls = ""

    sas_row_write_regex_case_one = re.compile(r"NOTE: Table (.*)\.(.*) created, with (\d+) rows")
    sas_row_write_regex_case_one_list = sas_row_write_regex_case_one.findall(record_content)
    sas_row_write_regex_case_one_list = [(record[2], record[0], record[1]) for record in
                                         sas_row_write_regex_case_one_list]

    sas_row_write_regex_case_two = re.compile(r"NOTE: (\d+) rows were deleted from (.*)\.(.*).")
    sas_row_write_regex_case_two_list = sas_row_write_regex_case_two.findall(record_content)
    if len(sas_row_write_regex_case_two_list) != 0:
        for record in sas_row_write_regex_case_two_list:
            if record[0] == 'No':
                record[0] = '0'
            rows = ';'.join([rows, str(record[0])])
            libs = ';'.join([libs, str(record[1])])
            tbls = ';'.join([tbls, str(record[2])])

    for record in sas_row_write_regex_case_one_list:
        rows = ';'.join([rows, str(record[0])])
        libs = ';'.join([libs, str(record[1])])
        tbls = ';'.join([tbls, str(record[2])])

    if rows == "":
        return None, None, None
    else:
        return rows[1:], libs[1:], tbls[1:]


def proc_sql_parsing(record_content):
    proc_sql_regex = re.compile(r"(.* INFO .*proc sql)(.+)((?:\n.+)+)(quit?|run?)", re.IGNORECASE)
    proc_sql_regex_list = proc_sql_regex.findall(record_content)

    input_library = []
    input_table = []
    output_library = []
    output_table = []

    if len(proc_sql_regex_list) != 0:
        sql_block = proc_sql_regex_list[0][0] + proc_sql_regex_list[0][2] + proc_sql_regex_list[0][3]
        proc_sql = get_proc_sql(sql_block)

        input_library, input_table = get_input_table_from_sql(proc_sql)

        output_library, output_table = get_output_table_from_sql(proc_sql)

    return input_library, input_table, output_library, output_table


# get proc sql from sql block
def get_proc_sql(sql_block):
    sql_lines = ""

    # MPRINT proc sql case: MPRINT(FCF_MAIN_PROCESS.FCF_PREP.FCF_CREATE_ASC_TRANS_VIEW):   proc sql noprint;
    if sql_lines == "":
        proc_sql_mprint_regex = re.compile(r"(MPRINT\(.*\)\:)(.+)((?:\n.+)+)(NOTE|quit)", re.IGNORECASE)
        proc_sql_mprint_regex_list = proc_sql_mprint_regex.findall(sql_block)
        if len(proc_sql_mprint_regex_list) >= 1:
            sql_lines = proc_sql_mprint_regex_list[0][1].strip() + " "

            mprint_regex = re.compile(r".* - MPRINT\(.*\)\:\s+(.*)")
            general_regex = re.compile(r".* - (.*)")

            mprint_block = proc_sql_mprint_regex_list[0][2]
            for mprint_block_line in mprint_block.splitlines():

                # if 'connect to' in mprint_block_line:
                #     sql_lines = 'pass through'
                #     break
                if '/*' in mprint_block_line or '/**' in mprint_block_line:
                    continue

                if re.match(mprint_regex, mprint_block_line) is not None:
                    mprint_block_line_list = mprint_regex.findall(mprint_block_line)
                else:
                    mprint_block_line_list = general_regex.findall(mprint_block_line)
                # print(mprint_block_line_list)
                if len(mprint_block_line_list) == 1 and mprint_block_line_list != '' and mprint_block_line_list[0][
                                                                                         :4] != 'NOTE' and \
                        mprint_block_line_list[0][:4] != 'SYMB':
                    sql_lines += mprint_block_line_list[0]

    # +proc sql case: hiragana - 874       +proc sql;
    if sql_lines == "":
        sql_block_regex = re.compile(r"(.* - \d+ \s+\+)(.*)")
        for sql_block_line in sql_block.splitlines():
            # if 'connect to' in sql_block_line:
            #     sql_lines = 'pass through'
            #     break
            if '/*' in sql_block_line or '/**' in sql_block_line:
                continue
            filtered_line = sql_block_regex.findall(sql_block_line)
            # print(filtered_line)
            if len(filtered_line) == 1 and len(filtered_line[0]) == 2 and filtered_line[0][1] != '':
                sql_lines += filtered_line[0][1].strip() + " "

    # number proc sql case: Bank2BU@SASBAP - 31         proc sql
    if sql_lines == "":
        proc_sql_num_regex = re.compile(r".* - \d+\s+(.*)")
        for sql_block_line in sql_block.splitlines():
            # if 'connect to' in sql_block_line:
            #     sql_lines = 'pass through'
            #     break
            if '/*' in sql_block_line or '/**' in sql_block_line:
                continue
            filtered_line = proc_sql_num_regex.findall(sql_block_line)

            if len(filtered_line) == 1 and filtered_line[0] != '':
                sql_lines += filtered_line[0].strip() + " "

    if len(sql_lines) > 0 and sql_lines[0] == '!':
        sql_lines = sql_lines[1:].strip()

    if "The SAS System" in sql_lines:
        sql_lines_list = re.split(r"The SAS System.*? \d\d\, \d\d\d\d ", sql_lines)
        sql_lines = "".join(sql_lines_list)

    return sql_lines + ' quit;'


# get input tables from SAS statement
def get_input_table_from_sql(proc_sql):
    input_library = []
    input_table = []
    lib_table_list = []

    if 'connect to' in proc_sql or 'CONNECT TO' in proc_sql:
        return input_library, input_table

    if 'union' in proc_sql:
        sql_union_regex = re.compile(r"from (.*?) ")
        lib_table_list = sql_union_regex.findall(proc_sql)

    if 'join' in proc_sql:

        # part 1: from ~
        sql_from_regex = re.compile(r"from (.*?) ")
        sql_from_list = sql_from_regex.findall(proc_sql)
        lib_table_list.append(sql_from_list[0])

        # part 2: xxx join ~
        if 'join (' in proc_sql:
            sql_join_regex = re.compile(r"join \(.* from (.*?\..*?)\) ")
            sql_join_list = sql_join_regex.findall(proc_sql)

        else:
            sql_join_regex = re.compile(r"join (.*?) ")
            sql_join_list = sql_join_regex.findall(proc_sql)

        lib_table_list += sql_join_list

    sql_from_where_regex = re.compile(r"from (.*?) where ", re.IGNORECASE)
    sql_from_where_list = sql_from_where_regex.findall(proc_sql)

    sql_from_order_regex = re.compile(r"from (.*?) order", re.IGNORECASE)
    sql_from_order_list = sql_from_order_regex.findall(proc_sql)

    sql_from_semi_regex = re.compile(r"from (.*?)(;| )", re.IGNORECASE)
    sql_from_semi_list = sql_from_semi_regex.findall(proc_sql)

    sql_from_quit_regex = re.compile(r"from (.*?) quit;", re.IGNORECASE)
    sql_from_quit_list = sql_from_quit_regex.findall(proc_sql)

    # case 1: "from (.*?) where "
    if len(sql_from_where_list) != 0 and len(lib_table_list) == 0:

        # check1 whether from is in values
        is_from_in_bracket_regex = re.compile(r'(.*?)from ', re.IGNORECASE)
        from_in_bracket_list = is_from_in_bracket_regex.findall(proc_sql)

        prior_from = from_in_bracket_list[0]
        sql_from_where_list_filtered = []

        if prior_from.count('(') == prior_from.count(')'):
            sql_from_where_list_filtered.append(sql_from_where_list[0])

        if len(sql_from_where_list_filtered) != 0:
            lib_table_list += sql_from_where_list_filtered

    # case 2: "from (.*?) order"
    elif len(sql_from_order_list) != 0 and len(lib_table_list) == 0:

        # check1 whether from is in brackets
        is_from_in_values_regex = re.compile(r'\(.*from.*\)', re.IGNORECASE)
        if re.search(is_from_in_values_regex, proc_sql) is not None:
            sql_from_order_list = []

        if len(sql_from_order_list) != 0:
            lib_table_list += sql_from_order_list[0].split(',')

    # case 3: "from (.*?)(;| )"
    elif len(sql_from_semi_list) != 0 and len(lib_table_list) == 0:

        # check1 whether from is in values
        is_from_in_values_regex = re.compile(r' values\(.*? from .*?\)', re.IGNORECASE)
        if re.search(is_from_in_values_regex, proc_sql) is not None:
            sql_from_semi_list = []

        lib_table_list += sql_from_semi_list
        lib_table_list = [element[0] for element in lib_table_list if element[0] != ""]

    # case4: "from (.*?) quit;"
    elif len(sql_from_quit_list) != 0 and len(lib_table_list) == 0:

        # check1 whether from is in values
        is_from_in_values_regex = re.compile(r' values\(.*? from .*?\)', re.IGNORECASE)
        if re.search(is_from_in_values_regex, proc_sql) is not None:
            sql_from_quit_list = []

        lib_table_list += sql_from_quit_list

    if len(lib_table_list) != 0:
        each_lib_table_list = []
        for lib_table in lib_table_list:
            each_lib_table_list += lib_table.split(',')

        seen = set()
        seen_add = seen.add
        each_lib_table_list = [x for x in each_lib_table_list if not (x in seen or seen_add(x))]

        for table in each_lib_table_list:
            if len(table) != 0:
                table = table.strip()
                table = table.split(' as ')[0]
                table = table.split(' ')[0]
                table = table.split('.')

            if len(table) == 1 and table[0] not in input_table:
                input_library.append('work')
                input_table.append(table[0])
            elif table[1] not in input_table:
                input_library.append(table[0])
                input_table.append(table[1])

    return input_library, input_table


# get output tables from SAS statement
def get_output_table_from_sql(proc_sql):
    output_library = []
    output_table = []

    sql_view_regex = re.compile(r"create view (.*?) ")
    lib_table_list = sql_view_regex.findall(proc_sql)

    sql_table_regex = re.compile(r"create table (.*?) ")
    lib_table_list += sql_table_regex.findall(proc_sql)

    if len(lib_table_list) != 0:
        for table in lib_table_list:
            if len(table) != 0:
                table = table.strip()
                table = table.split(' as ')[0]
                table = table.split(' ')[0]
                table = table.split('.')
            if len(table) == 1 and table[0] not in output_table:
                output_library.append('work')
                output_table.append(table[0])
            elif len(table) > 1 and table[1] not in output_table:
                output_library.append(table[0])
                output_table.append(table[1])

    return output_library, output_table


# get input library,input table, output library and output table from SAS statement
def data_step_parsing(record_content):
    data_step_regex = re.compile(r"(.* INFO .*data)(.+?)((?:\n.+)+)(run)", re.IGNORECASE)
    data_step_regex_list = data_step_regex.findall(record_content)

    input_library = []
    input_table = []
    output_library = []
    output_table = []

    if len(data_step_regex_list) != 0:
        sql_block = data_step_regex_list[0][0] + data_step_regex_list[0][1] + data_step_regex_list[0][2] + \
                    data_step_regex_list[0][3] + ';'

        data_step_sql = get_data_step_sql(sql_block)

        input_library, input_table = get_input_table_from_data_sql(data_step_sql)
        output_library, output_table = get_output_table_from_data_sql(data_step_sql)

    return input_library, input_table, output_library, output_table


# get data step from sql block
def get_data_step_sql(sql_block):
    sql_lines = ""

    # MPRINT proc sql case: :hxdhiraj - MPRINT(ETLS_LOADER):   data
    if sql_lines == "":
        data_step_sql_mprint_regex = re.compile(r"(.*MPRINT\(.*\)\:\s+data )(.+?)((?:\n.+)+)( run)", re.IGNORECASE)
        data_step_sql_mprint_regex_list = data_step_sql_mprint_regex.findall(sql_block)
        if len(data_step_sql_mprint_regex_list) >= 1:
            sql_lines = "data " + data_step_sql_mprint_regex_list[0][1].strip() + " "

            mprint_regex = re.compile(r".* INFO .* - MPRINT\(.*\)\:\s+(.*)")
            general_regex = re.compile(r".* INFO .* - (.*)")

            mprint_block = data_step_sql_mprint_regex_list[0][2]
            for mprint_block_line in mprint_block.splitlines():

                # if 'connect to' in mprint_block_line:
                #     sql_lines = 'pass through'
                #     break
                if 'The SAS System' in mprint_block_line or '/*' in mprint_block_line or 'NOTE' in mprint_block_line:
                    continue

                if re.match(mprint_regex, mprint_block_line) is not None:
                    mprint_block_line_list = mprint_regex.findall(mprint_block_line)
                else:
                    mprint_block_line_list = general_regex.findall(mprint_block_line)

                if len(mprint_block_line_list) == 1 and mprint_block_line_list != '' and \
                        mprint_block_line_list[0][:4] != 'SYMB':
                    sql_lines += mprint_block_line_list[0]
            sql_lines += ' run;'

    # number + case :  - 1354      +set DmdMgt.GEOBRANDSUPADDS(where=(country_code='US'));
    if sql_lines == "":

        plus_data_step_regex = re.compile(r"(.*\+\s*data)(.+?)((?:\n.*)*)(run)", re.IGNORECASE)
        plus_data_step_regex_list = plus_data_step_regex.findall(sql_block)

        if len(plus_data_step_regex_list) != 0:
            plus_sql_block = plus_data_step_regex_list[0][0] + plus_data_step_regex_list[0][1] + \
                             plus_data_step_regex_list[0][2] + \
                             plus_data_step_regex_list[0][3]

            sql_block_regex = re.compile(r"(.* INFO .* - \d+ \s+\+)(.*)")
            for sql_block_line in plus_sql_block.splitlines():
                # if 'connect to' in sql_block_line:
                #     sql_lines = 'pass through'
                #     break
                if 'The SAS System' in sql_block_line or '/*' in sql_block_line or 'NOTE' in sql_block_line or \
                        'value(s) will be set' in sql_block_line:
                    continue
                filtered_line = sql_block_regex.findall(sql_block_line)
                if len(filtered_line) == 1 and len(filtered_line[0]) == 2 and filtered_line[0][1] != '':
                    sql_lines += filtered_line[0][1].strip() + " "

    # number data step sql case: :hxdhiraj - 673        data
    if sql_lines == "":

        num_data_step_regex = re.compile(r"(.*  data)(.+?)((?:\n.+)+)(run)", re.MULTILINE)
        num_data_step_regex_list = num_data_step_regex.findall(sql_block)

        if len(num_data_step_regex_list) != 0:
            num_sql_block = num_data_step_regex_list[0][0] + num_data_step_regex_list[0][1] + \
                            num_data_step_regex_list[0][2] + \
                            num_data_step_regex_list[0][3]

            data_step_sql_num_regex = re.compile(r".* INFO .* - \d+\s+(.*)")
            for sql_block_line in num_sql_block.splitlines():
                # if 'connect to' in sql_block_line:
                #     sql_lines = 'pass through'
                #     break
                if 'The SAS System' in sql_block_line or '/*' in sql_block_line or 'NOTE' in sql_block_line:
                    continue

                filtered_line = data_step_sql_num_regex.findall(sql_block_line)

                if len(filtered_line) == 1 and filtered_line[0] != '':
                    sql_lines += filtered_line[0].strip() + " "

            splited_sql = sql_lines.split("!")
            if len(splited_sql) == 2:
                sql_lines = splited_sql[1].strip()
            else:
                sql_lines = splited_sql[0]

    return sql_lines


# get input library and input table
def get_input_table_from_data_sql(data_step_sql):
    input_lib = []
    input_table = []

    set_lib_table_list = []
    merge_lib_table_list = []
    update_lib_table_list = []

    # get input library and table from set
    set_between_quote_regex = re.compile(r"\".*? set .*\"")

    if re.search(set_between_quote_regex, data_step_sql) is None:
        set_regex = re.compile(r"[;| ]set (.*?)(;|\(| )")
        set_lib_table_list = set_regex.findall(data_step_sql)

        set_lib_table_list = [element[0] for element in set_lib_table_list if element[0] != ""]

    # get input library and table from merge
    merge_regex = re.compile(r"merge (.*?);")
    if re.search(merge_regex, data_step_sql) is not None:
        merge_regex_list = merge_regex.findall(data_step_sql)
        merge_lib_table_regex = re.compile(r"(.*?)(\(.*\) | \(.*\)| )")
        merge_lib_table_list = merge_lib_table_regex.findall(merge_regex_list[0])
        merge_lib_table_list = [element[0] for element in merge_lib_table_list if element[0] != ""]

        # exception case 1 : if merge is between quotes
        merge_between_quote_regex = re.compile(r"\".*?merge .*?\"")
        if re.search(merge_between_quote_regex, data_step_sql) is not None:
            merge_lib_table_list = []

    # need to work with 'UPDATE'
    update_regex = re.compile(r"update (.*?);")
    if re.search(update_regex, data_step_sql) is not None:
        update_regex_list = update_regex.findall(data_step_sql)
        update_lib_table_regex = re.compile(r"(.*?)(\(.*\) | \(.*\)| )")
        update_lib_table_list = update_lib_table_regex.findall(update_regex_list[0])
        update_lib_table_list = [element[0] for element in update_lib_table_list if element[0] != ""]

        # exception case 1 : if update is between quotes
        update_between_quote_regex = re.compile(r"\".*?update .*?\"")
        if re.search(update_between_quote_regex, data_step_sql) is not None:
            update_lib_table_list = []

    input_regex_list = set_lib_table_list + merge_lib_table_list + update_lib_table_list

    if len(input_regex_list) != 0:

        for table in input_regex_list:
            if table != "":
                table = table.strip()
                table = table.split(' as ')[0]
                table = table.split(' ')[0]
                table = table.split('.')
            if len(table) == 1 and table[0] not in input_table:
                input_lib.append('work')
                input_table.append(table[0])
            elif len(table) == 1 and table[0] in input_table:
                continue
            elif table[1] not in input_table:
                input_lib.append(table[0])
                input_table.append(table[1])

    return input_lib, input_table


# get output library and output table
def get_output_table_from_data_sql(data_step_sql):
    output_lib = []
    output_table = []

    data_out_tbl_regex = re.compile(r"data (.*?);")
    data_out_tbl_list = data_out_tbl_regex.findall(data_step_sql)
    data_out_bracket_list = []
    data_out_space_list = []
    data_out_view_list = []

    if len(data_out_tbl_list) != 0:

        if '_null_' in data_out_tbl_list[0]:
            data_out_tbl_list = []
        else:
            data_out_string = data_out_tbl_list[0]
            data_out_tbl_list = []

            if " " not in data_out_string:
                data_out_tbl_list.append(data_out_string)

            if '(' in data_out_string:
                data_out_tbl_regex = re.compile(r"(.*?)(\(.*?\)| )")
                data_out_bracket_list = data_out_tbl_regex.findall(data_out_string)
                if len(data_out_bracket_list) != 0:
                    data_out_bracket_list = [element[0] for element in data_out_bracket_list if '.' in element[0]]

            elif ' ' in data_out_string and '/view' not in data_out_string:
                data_out_space_list = data_out_string.split(" ")

            elif ' ' in data_out_string and '/view' in data_out_string:
                data_out_space_list = [data_out_string.split(" ")[0]]

            if '/view' in data_out_string:
                data_out_view_list = [data_out_string.split("=")[-1]]

    data_out_tbl_list = data_out_tbl_list + data_out_bracket_list + data_out_space_list + data_out_view_list

    if len(data_out_tbl_list) != 0:

        for table in data_out_tbl_list:

            if table == "":
                continue

            if len(table) != 0:
                table = table.strip()
                table = table.split(' as ')[0]
                table = table.split(' ')[0]
                table = table.split('.')

                if len(table) == 1 and table[0] not in output_table:
                    output_lib.append('work')
                    output_table.append(table[0])
                elif len(table) == 1 and table[0] in output_table:
                    continue
                elif table[1] not in output_table:
                    output_lib.append(table[0])
                    output_table.append(table[1])

    return output_lib, output_table


# write SAS library and SAS table to variable FILE_SAS_LIB, FILE_SAS_TBL
def lib_table_write_to_variable(library, table, FILE_SAS_LIB, FILE_SAS_TBL):
    if table and len(table) != 0:

        # filter out exceptional cases such as table name ended with ()
        filtered_table = []
        for table_name in table:
            if table_name[-2:] == '()':
                filtered_table.append(table_name[:-2])
            else:
                filtered_table.append(table_name)

        if FILE_SAS_TBL == "":
            FILE_SAS_LIB = ';'.join(library)
            FILE_SAS_TBL = ';'.join(filtered_table)
        else:
            for lib, tbl in zip(library, filtered_table):
                if tbl.lower() not in FILE_SAS_TBL and tbl.upper() not in FILE_SAS_TBL:
                    FILE_SAS_LIB += ";" + lib
                    FILE_SAS_TBL += ";" + tbl

    return FILE_SAS_LIB, FILE_SAS_TBL


# if Marco used in SAS step, return 1, otherwise return 0
def get_macro_flag(FILE_SAS_INP_LIB, FILE_SAS_INP_TBL, FILE_SAS_OUT_LIB, FILE_SAS_OUT_TBL):
    lib_tbl_str = FILE_SAS_INP_LIB + ';' + FILE_SAS_INP_TBL + ';' + FILE_SAS_OUT_LIB + ';' + FILE_SAS_OUT_TBL
    lib_tbl_list = lib_tbl_str.split(';')
    for lib_or_tbl in lib_tbl_list:
        if "&" in lib_or_tbl:
            return 1
    return 0


# 1. check the record_contest has a libname ABC oracle/db2/hadoop/etc
# 2. if the database type is not base or V9 save it to ext_db_lib_ref_list
# 3.     ext_db_ref_list is created based on each file as empty list
#        return the name of the database name
# 4. on main function, check proc sql in / out part before save it to pandas.
def get_ext_db(record_content):
    ext_db_name_list = []
    # Check with proc sql statement
    proc_sql_regex = re.compile(r"(.* INFO .*proc sql)(.+)((?:\n.+)+)(quit?|run?)", re.IGNORECASE)
    proc_sql_regex_list = proc_sql_regex.findall(record_content)
    if len(proc_sql_regex_list) != 0:
        sql_block = proc_sql_regex_list[0][0] + proc_sql_regex_list[0][2] + proc_sql_regex_list[0][3]
        proc_sql = get_proc_sql(sql_block)

        if "connect to" in proc_sql:
            ext_db_regex = re.compile(r"connect to (.*?)(\(| )")
            ext_db_obj = ext_db_regex.search(proc_sql)
            ext_db_name = ext_db_obj.group(1)
            ext_db_name_list.append(ext_db_name.lower())

    lib_name_list, db_name_list = ext_db_checker(record_content)

    ext_db_name_list += db_name_list
    ext_db_name_list = list(set(ext_db_name_list))

    return ext_db_name_list


# Record library_reference, engine_name and library_statement
def ext_db_checker(record_content):
    external_database_tuple = (
        'redshift', 'aster', 'db2' 'bigquery', 'greenplm', 'hadoop', 'hawq', 'impala', 'informix', 'jdbc', 'sqlsvr',
        'mysql', 'netezza', 'odbc', 'oledb', 'oracle', 'postgres', 'sapase', 'saphana', 'sapiq', 'snow', 'spark',
        'teradata', 'vertica', 'ybrick', 'mongo', 'sforce'
    )
    library_name_list = []
    database_name_list = []

    libname_regex = re.compile(r"libname (\w+?) (\w+?)(;| )", re.IGNORECASE)
    libname_list = libname_regex.findall(record_content)

    if libname_list:
        for lib_db in libname_list:

            temp_library_name = lib_db[0]
            temp_database_name = lib_db[1].lower()

            if temp_database_name in external_database_tuple:
                library_name_list.append(temp_library_name)
                database_name_list.append(temp_database_name)

    return library_name_list, database_name_list


# get migration disposition based on SAS statement
def get_migration_disp(FILE_SAS_EXC_CPU_TM, FILE_SAS_EXC_RL_TM, FILE_SAS_STP, FILE_SAS_STP_NM, record_content):
    RULE_ID = ""
    REC_ACT = ""
    recommendation = "Lift and Shift"

    data_statement = ""

    data_step_regex = re.compile(r"(.* INFO .* data)(.+?)((?:\n.+)+)(run)", re.IGNORECASE)
    data_step_regex_list = data_step_regex.findall(record_content)

    if len(data_step_regex_list) != 0:
        sql_block = data_step_regex_list[0][0] + data_step_regex_list[0][1] + data_step_regex_list[0][2] + \
                    data_step_regex_list[0][3]
        data_statement = get_data_step_sql(sql_block)

    proc_sql = ""
    proc_sql_regex = re.compile(r"(.* INFO .*proc sql)(.+)((?:\n.+)+)(quit?|run?)", re.IGNORECASE)
    proc_sql_regex_list = proc_sql_regex.findall(record_content)

    if len(proc_sql_regex_list) != 0:
        sql_block = proc_sql_regex_list[0][0] + proc_sql_regex_list[0][2] + proc_sql_regex_list[0][3]
        proc_sql = get_proc_sql(sql_block)

    if FILE_SAS_EXC_CPU_TM >= 30.00:
        recommendation = "Code Change"
        RULE_ID = '1'
        REC_ACT = 'Consider reducing real time'
    elif FILE_SAS_EXC_CPU_TM >= FILE_SAS_EXC_RL_TM and FILE_SAS_EXC_CPU_TM != 0:
        recommendation = "Code Change"
        RULE_ID = '2'
        REC_ACT = 'Consider reducing cpu time so that it is less then real time'
    elif FILE_SAS_STP == 'PROCEDURE Statement' and FILE_SAS_STP_NM == 'LOGISTIC':
        recommendation = "Code Change"
        RULE_ID = '4'
        REC_ACT = 'Consider using PROC LOGSELECT (CAS) instead of Logistic'
    elif FILE_SAS_STP == 'PROCEDURE Statement' and FILE_SAS_STP_NM == 'MIXED':
        recommendation = "Code Change"
        RULE_ID = '5'
        REC_ACT = 'Consider using PROC LMIXED (CAS) instead of Mixed'
    elif FILE_SAS_STP == 'PROCEDURE Statement' and FILE_SAS_STP_NM == 'REG':
        recommendation = "Code Change"
        RULE_ID = '6'
        REC_ACT = 'Consider using PROC REGSELECT (CAS) instead of Reg'
    elif FILE_SAS_STP == 'PROCEDURE Statement' and FILE_SAS_STP_NM == 'SQL':
        recommendation = "Code Change"
        RULE_ID = '9'
        REC_ACT = 'Push Down whenever possible.'
    elif FILE_SAS_STP == 'PROCEDURE Statement' and FILE_SAS_STP_NM == 'SORT':
        recommendation = "Code Change"
        RULE_ID = '10'
        REC_ACT = 'Push Down whenever possible. (To save memory use partioning)'
    elif FILE_SAS_STP == 'PROCEDURE Statement' and FILE_SAS_STP_NM == 'TRANSPOSE':
        recommendation = "Code Change"
        RULE_ID = '11'
        REC_ACT = 'Depending on ther data source stays as DB2 or moves to native cloud data base.'
    elif FILE_SAS_STP == 'PROCEDURE Statement' and FILE_SAS_STP_NM == 'FORMAT':
        recommendation = "Code Change"
        RULE_ID = '12'
        REC_ACT = 'Depending on ther data source stays as DB2 or moves to native cloud data base.'
    elif FILE_SAS_STP == 'PROCEDURE Statement' and FILE_SAS_STP_NM == 'FEDSQL':
        recommendation = "Code Change"
        RULE_ID = '13'
        REC_ACT = 'Code Change because PROC FedSQL is ANSI 99 SQL compliant'
    elif FILE_SAS_STP == 'PROCEDURE Statement' and FILE_SAS_STP_NM == 'APPEND':
        recommendation = "Code Change"
        RULE_ID = '14'
        REC_ACT = 'Neglect if target CAS table exists prior to the PROC APPEND.'
    elif FILE_SAS_STP == 'DATA statement' and 'index' in data_statement.lower():
        recommendation = "Code Change"
        RULE_ID = '15'
        REC_ACT = 'Neglect INDEX in DATA STATEMENT because its Obsoleted since there are no more pointers available to indicate specific rows due to data allocated to different cores and threads.'
    elif FILE_SAS_STP == 'DATA statement' and 'firstobs' in data_statement.lower():
        recommendation = "Code Change"
        RULE_ID = '16'
        REC_ACT = 'Neglect FIRSTOBS in DATA STATEMENT because its Obsoleted since there are no more pointers available to indicate specific rows due to data allocated to different cores and threads.'
    elif FILE_SAS_STP == 'DATA statement' and 'obs' in data_statement.lower():
        recommendation = "Code Change"
        RULE_ID = '17'
        REC_ACT = 'Neglect OBS in DATA STATEMENT because its Obsoleted since there are no more pointers available to indicate specific rows due to data allocated to different cores and threads.'
    elif FILE_SAS_STP == 'DATA statement' and 'pointobs' in data_statement.lower():
        recommendation = "Code Change"
        RULE_ID = '18'
        REC_ACT = 'Neglect POINTOBS in DATA STATEMENT because its Obsoleted since there are no more pointers available to indicate specific rows due to data allocated to different cores and threads.'
    elif FILE_SAS_STP == 'DATA statement' and 'infile' in data_statement.lower():
        recommendation = "Code Change"
        RULE_ID = '19'
        REC_ACT = 'Replace with SET statements, with the new SET statements pointing to the correct in-memory tables.'
    elif FILE_SAS_STP == 'DATA statement' and 'input' in data_statement.lower():
        recommendation = "Code Change"
        RULE_ID = '20'
        REC_ACT = 'Replace with SET statements, with the new SET statements pointing to the correct in-memory tables.'
    elif FILE_SAS_STP == 'DATA statement' and 'datalines' in data_statement.lower():
        recommendation = "Code Change"
        RULE_ID = '21'
        REC_ACT = 'Replace with SET statements, with the new SET statements pointing to the correct in-memory tables.'
    elif FILE_SAS_STP == 'DATA statement' and 'varfmt' in data_statement.lower():
        recommendation = "Code Change"
        RULE_ID = '22'
        REC_ACT = ''
    elif FILE_SAS_STP == 'PROCEDURE Statement' and 'varfmt' in proc_sql.lower():
        recommendation = "Code Change"
        RULE_ID = '22'
        REC_ACT = 'Neglect VARFMT function because it is Obsolete.'
    elif FILE_SAS_EXC_CPU_TM >= FILE_SAS_EXC_RL_TM and FILE_SAS_EXC_CPU_TM >= 10:
        recommendation = "Code Change"
        RULE_ID = '23'
        REC_ACT = 'new rule: Consider reducing cpu time so that it is less then real time'

    return REC_ACT, RULE_ID, recommendation


# get migration rule accoring to migration rule ID
def get_migr_rule(FILE_SAS_MIGR_RUL_ID, migr_rule_dict):
    if FILE_SAS_MIGR_RUL_ID == "":
        return ""

    migration_rule = migr_rule_dict.get(FILE_SAS_MIGR_RUL_ID)
    return migration_rule


# if in-memory procedure used, return 1, otherwise return 0
def get_proc_inmem(record_content, FILE_SAS_STP, FILE_SAS_STP_NM, inmem_tuple):

    for keyword in inmem_tuple:
        if keyword in record_content.upper():
            return 1

    if FILE_SAS_STP == "PROCEDURE Statement" and (FILE_SAS_STP_NM == 'LASR' or FILE_SAS_STP_NM == 'IAMSTAT'):
        return 1
    else:
        return 0


# if ETL Procedure used, return 1, otherwise return 0
def get_proc_etl(FILE_SAS_PROC_CAT, FILE_SAS_STP, FILE_SAS_STP_NM):
    if FILE_SAS_PROC_CAT == 'Data Management' and FILE_SAS_STP == 'PROCEDURE Statement' and FILE_SAS_STP_NM in [
        "APPEND", "CONTESTS", "DATASETS", "SORT", "SQL", "IMPORT"]:
        return 1
    else:
        return 0


# if grid procedure used, return 1, otherwise return 0
def get_proc_grid(record_content, proc_grid_tuple):
    for keyword in proc_grid_tuple:
        if keyword in record_content.upper():
            return 1
    return 0


# get if database is external, return 1, otherwise return 0
def get_indb(record_content):
    external_database_tuple = (
        'redshift', 'aster', 'db2' 'bigquery', 'greenplm', 'hadoop', 'hawq', 'impala', 'informix', 'jdbc', 'sqlsvr',
        'mysql', 'netezza', 'odbc', 'oledb', 'oracle', 'postgres', 'sapase', 'saphana', 'sapiq', 'snow', 'spark',
        'teradata', 'vertica', 'ybrick', 'mongo', 'sforce'
    )

    connect_db_regex = re.compile(r"connect to (.*?)[ |\(]", re.IGNORECASE)
    connect_db_list = connect_db_regex.findall(record_content)

    disconnect_db_regex = re.compile(r"disconnect from (.*?)[;| ]", re.IGNORECASE)
    disconnect_db_list = disconnect_db_regex.findall(record_content)

    if len(connect_db_list) != 0:
        for conn_db, disconn_db in zip(connect_db_list, disconnect_db_list):
            if conn_db == disconn_db and conn_db in external_database_tuple:
                return 1
    return 0


# update a row of record to the given dataframe 'log_df'
def save_record_to_df(log_df, extracted_record):
    updated_log_df = log_df.append(pd.Series(extracted_record, index=log_df.columns), ignore_index=True)
    return updated_log_df


# save the dataframe to an excel file
def save_df_to_xlsx(log_df):
    # check "\output" folder and make it if it is not exist
    if platform.system() == 'Windows':
        if not os.path.isdir('..\\Data_Model\\Extracted_Files'):
            os.makedirs('..\\Data_Model\\Extracted_Files')

        log_df.to_excel("..\\Data_Model\\Extracted_Files\\D_CLDASST_DISC_LOG_O.xlsx", float_format="%0.2f", index=False)
        log_df.to_csv("..\\Data_Model\\Extracted_Files\\D_CLDASST_DISC_LOG_O.csv", float_format="%0.2f", index=False,
                  date_format='%Y-%m-%d %H:%M:%S')
    else:

        if not os.path.isdir('../Data_Model/Extracted_Files'):
            os.makedirs('../Data_Model/Extracted_Files')

        log_df.to_excel("../Data_Model/Extracted_Files/D_CLDASST_DISC_LOG_O.xlsx", float_format="%0.2f", index=False)
        log_df.to_csv("../Data_Model/Extracted_Files/D_CLDASST_DISC_LOG_O.csv", float_format="%0.2f", index=False,
                      date_format='%Y-%m-%d %H:%M:%S')

# main function
if __name__ == "__main__":

    FILE_ID = ""
    FILE_PTH = ""
    FILE_NM = ""
    FILE_USR_NM = ""
    FILE_SAS_F_ID = ""
    FILE_SAS_F_LOC = ""
    FILE_SAS_F_NM = ""
    FILE_SAS_STP = ""
    FILE_SAS_STP_NM = ""
    FILE_LN_NUM = ""
    FILE_SAS_INP_LIB = ""
    FILE_SAS_INP_TBL = ""
    FILE_SAS_INP_FIL_NM = ""
    FILE_SAS_INP_ROW_RD = 0
    FILE_SAS_OUT_LIB = ""
    FILE_SAS_OUT_TBL = ""
    FILE_SAS_ROW_WRT = 0
    FILE_SAS_INP_MUL_FLG = ""
    FILE_SAS_INP_MUL_TBLS = ""
    FILE_SAS_MACRO_FLG = ""
    FILE_SAS_EXT_DB = ""
    FILE_EXC_DT = ""
    FILE_SAS_EXC_TM = ""
    FILE_SAS_EXC_CPU_TM = ""
    FILE_SAS_EXC_RL_TM = ""
    FILE_SAS_PROC_CAT = ""
    FILE_SAS_PROC_PROD = ""
    FILE_SAS_MIGR_DISP = ""
    FILE_SAS_MIGR_RUL_ID = ""
    FILE_SAS_MIGR_RUL = ""
    FILE_SAS_MIGR_REC_ACT = ""
    FILE_SAS_PROC_INMEM_FLG = 0
    FILE_SAS_PROC_ELT_FLG = 0
    FILE_SAS_PROC_GRID_FLG = 0
    FILE_SAS_PROC_INDB_FLG = 0
    FILE_SAS_SRC_TYP = "SAS"
    FILE_SAS_ENV_NAME = "SAS GRID PROD"

    # Define columns name for .csv and .xlxs file
    log_df = pd.DataFrame(columns=['FILE_ID', 'FILE_PTH', 'FILE_NM', 'FILE_USR_NM', 'FILE_SAS_F_ID',
                                   'FILE_SAS_F_LOC', 'FILE_SAS_F_NM', 'FILE_SAS_STP',
                                   'FILE_SAS_STP_NM', 'FILE_LN_NUM', 'FILE_SAS_INP_LIB',
                                   'FILE_SAS_INP_TBL', 'FILE_SAS_INP_FIL_NM', 'FILE_SAS_INP_ROW_RD',
                                   'FILE_SAS_OUT_LIB', 'FILE_SAS_OUT_TBL', 'FILE_SAS_ROW_WRT',
                                   'FILE_SAS_INP_MUL_FLG', 'FILE_SAS_INP_MUL_TBLS', 'FILE_SAS_MACRO_FLG',
                                   'FILE_SAS_EXT_DB', 'FILE_EXC_DT',
                                   'FILE_SAS_EXC_TM', 'FILE_SAS_EXC_CPU_TM', 'FILE_SAS_EXC_RL_TM',
                                   'FILE_SAS_PROC_CAT', 'FILE_SAS_PROC_PROD', 'FILE_SAS_MIGR_DISP',
                                   'FILE_SAS_MIGR_RUL_ID', 'FILE_SAS_MIGR_RUL', 'FILE_SAS_MIGR_REC_ACT',
                                   'FILE_SAS_PROC_INMEM_FLG', 'FILE_SAS_PROC_ELT_FLG', 'FILE_SAS_PROC_GRID_FLG',
                                   'FILE_SAS_PROC_INDB_FLG', 'FILE_SAS_SRC_TYP', 'FILE_SAS_ENV_NAME'])
    # get current path
    current_path = os.getcwd()
    current_folder = 'logs'
    visited = dict()
    file_list = []
    cat_prod_dict = dict()
    cat_prod_dict = init_proc_cat_prod(cat_prod_dict)
    migr_rule_dict = init_migr_rule()
    inmem_tuple = init_inmem()
    proc_grid_tuple = init_proc_grid()
    # Get file names in 'Adapter/logs' folder in a recursive way
    # does not return a list. Instead, file_list has all the list of files as list is reference data type :)
    getInventory(current_path, current_folder, visited, file_list)
    file_id_counter = 1
    sas_file_id_counter = 1
    file_list = []
    # get sas file id
    sas_file_dict = get_sas_file_id(current_path, current_folder, visited,
                                    file_list)  # key: file name, value: FILE_SAS_F_ID

    for file_path, file_name in file_list:

        ext_db_lib_name_list = []

        if platform.system() == 'Windows':
            file_full_path = file_path + '\\' + file_name
        else:
            file_full_path = file_path + '/' + file_name

        # read log contents from given file_path
        log_content = get_log_content(file_full_path)
        FILE_PTH = file_full_path
        FILE_NM = file_name

        sas_file_content_list = get_sas_files(log_content)
        for sas_file_abs_path, sas_file_content in sas_file_content_list:

            temp_num = 1

            if re.search(r"cpu time .*? seconds\n.*? - \d+\s+The SAS System.*? \d\d\d\d", sas_file_content):
                sas_file_content = re.sub(r' \d+\s+The SAS System.*? \d\d\d\d', '       ', sas_file_content)
            else:
                sas_file_content = re.sub(r' \d+\s+The SAS System.*? \d\d\d\d', '              ', sas_file_content)

            record_content_list = re.split(r"seconds\n.*? -       \n", sas_file_content)

            for record_content in record_content_list:
                if record_content[-25:-17] != 'cpu time':
                    continue

                # print("record content num:" + str(temp_num))
                # temp_num+=1
                # print(record_content)
                # print("********************")

                # update sas file id and sas file name and path if it is updated.
                if sas_file_abs_path != '':
                    sas_file_norm_path = os.path.normpath(sas_file_abs_path)
                    FILE_SAS_F_NM = sas_file_norm_path.split(os.sep)[-1]
                    if sas_file_dict.get(FILE_SAS_F_NM) is None:
                        sas_file_dict[FILE_SAS_F_NM] = 'SF_' + str(sas_file_id_counter)
                        sas_file_id_counter += 1
                    FILE_SAS_F_ID = sas_file_dict.get(FILE_SAS_F_NM)

                # get all the user name of the given log file
                FILE_USR_NM = get_user_name(record_content)
                FILE_SAS_F_LOC = sas_file_abs_path
                if FILE_SAS_F_LOC == "":
                    FILE_SAS_F_NM = ""
                    FILE_SAS_F_ID = ""
                # get input file name such as .csv file
                FILE_SAS_INP_ROW_RD, FILE_SAS_INP_FIL_NM = get_input_file_name(record_content)
                if FILE_SAS_INP_FIL_NM != "":
                    FILE_SAS_INP_TBL = FILE_SAS_INP_FIL_NM.split('/')[-1]
                    FILE_SAS_INP_LIB = 'Ext'
                else:
                    # get input library and input table from regular log output such as NOTE:
                    FILE_SAS_INP_LIB, FILE_SAS_INP_TBL = get_input_library_table(record_content)
                # get output library and output table from regular log message such as NOTE:
                FILE_SAS_OUT_LIB, FILE_SAS_OUT_TBL = get_output_library_table(record_content)

                if FILE_SAS_F_LOC == "":
                    FILE_LN_NUM = ""
                else:
                    # get SAS file line number
                    FILE_LN_NUM = get_sas_file_line_number(record_content)
                # get SAS Step names such as DATA statement, Procedure SQL, SAS Initialization
                FILE_SAS_STP, FILE_SAS_STP_NM = get_sas_step_name(record_content)
                if FILE_SAS_STP == 'SAS Initialization' or FILE_SAS_STP == 'SAS System':
                    continue

                # Check if the FILE_SAS_STP is DATA and if it is not, initialize FILE_SAS_INP_ROW_RD and Input file
                if FILE_SAS_STP == 'PROCEDURE Statement':
                    FILE_SAS_INP_ROW_RD = FILE_SAS_INP_FIL_NM = ""
                # get time information
                FILE_EXC_DT, FILE_SAS_EXC_TM = get_time_info(record_content)

                FILE_SAS_EXC_CPU_TM, FILE_SAS_EXC_RL_TM = get_process_time(record_content)
                # get number of rows write and output library and output table.
                rows, libs, tbls = get_sas_row_write(record_content)
                if rows is not None:
                    FILE_SAS_ROW_WRT = rows
                    if FILE_SAS_OUT_LIB == "":
                        FILE_SAS_OUT_LIB = libs
                    else:
                        # use ";" to separate FILE_SAS_OUT_LIB and libs
                        FILE_SAS_OUT_LIB = ';'.join([FILE_SAS_OUT_LIB, libs])
                    if FILE_SAS_OUT_TBL == "":
                        FILE_SAS_OUT_TBL = tbls
                    else:
                        FILE_SAS_OUT_TBL = ';'.join([FILE_SAS_OUT_TBL, tbls])

                if FILE_SAS_STP == "PROCEDURE Statement":
                    input_lib, input_table, output_lib, output_table = proc_sql_parsing(record_content)
                else:
                    input_lib, input_table, output_lib, output_table = data_step_parsing(record_content)
                # write SAS library and SAS table to variable FILE_SAS_LIB, FILE_SAS_TBL
                FILE_SAS_INP_LIB, FILE_SAS_INP_TBL = lib_table_write_to_variable(input_lib, input_table,
                                                                                 FILE_SAS_INP_LIB,
                                                                                 FILE_SAS_INP_TBL)

                FILE_SAS_OUT_LIB, FILE_SAS_OUT_TBL = lib_table_write_to_variable(output_lib, output_table,
                                                                                 FILE_SAS_OUT_LIB,
                                                                                 FILE_SAS_OUT_TBL)
                # if Marco used in SAS step, return 1, otherwise return 0
                FILE_SAS_MACRO_FLG = get_macro_flag(FILE_SAS_INP_LIB, FILE_SAS_INP_TBL, FILE_SAS_OUT_LIB,
                                                    FILE_SAS_OUT_TBL)
                # 1. check the record_contest has a libname ABC oracle/db2/hadoop/etc
                # 2. if the database type is not base or V9 save it to ext_db_list
                #        return the name of the database name
                ext_db_list = get_ext_db(record_content)
                FILE_SAS_EXT_DB = ';'.join(ext_db_list)

                if FILE_SAS_STP_NM == 'DATA':
                    FILE_SAS_PROC_PROD, FILE_SAS_PROC_CAT = 'Base SAS', 'Data Management'
                elif FILE_SAS_STP_NM == '':
                    pass
                else:
                    proc_tuple = cat_prod_dict.get(FILE_SAS_STP_NM.upper())
                    if proc_tuple is not None:
                        FILE_SAS_PROC_PROD, FILE_SAS_PROC_CAT = proc_tuple
                    else:
                        FILE_SAS_PROC_PROD, FILE_SAS_PROC_CAT = 'Base SAS', 'Data Management'

                if len(FILE_SAS_INP_LIB.split(';')) > 1:
                    FILE_SAS_INP_MUL_FLG = 1
                    FILE_SAS_INP_MUL_TBLS = 1
                else:
                    FILE_SAS_INP_MUL_FLG = 0
                    FILE_SAS_INP_MUL_TBLS = 0
                # get migration disposition based on SAS statement
                FILE_SAS_MIGR_REC_ACT, FILE_SAS_MIGR_RUL_ID, FILE_SAS_MIGR_DISP = get_migration_disp(
                    FILE_SAS_EXC_CPU_TM, FILE_SAS_EXC_RL_TM,
                    FILE_SAS_STP, FILE_SAS_STP_NM,
                    record_content)
                # get migration rule according to migration rule ID
                FILE_SAS_MIGR_RUL = get_migr_rule(FILE_SAS_MIGR_RUL_ID, migr_rule_dict)
                # if in-memory procedure used, return 1, otherwise return 0
                FILE_SAS_PROC_INMEM_FLG = get_proc_inmem(record_content, FILE_SAS_STP, FILE_SAS_STP_NM, inmem_tuple)
                # if ETL Procedure used, return 1, otherwise return 0
                FILE_SAS_PROC_ELT_FLG = get_proc_etl(FILE_SAS_PROC_CAT, FILE_SAS_STP, FILE_SAS_STP_NM)
                # if grid procedure used, return 1, otherwise return 0
                FILE_SAS_PROC_GRID_FLG = get_proc_grid(record_content, proc_grid_tuple)
                # get if database is external, return 1, otherwise return 0
                FILE_SAS_PROC_INDB_FLG = get_indb(record_content)

                FILE_ID = 'LOG_' + str(file_id_counter)
                file_id_counter += 1
                extracted_record = [FILE_ID, FILE_PTH, FILE_NM, FILE_USR_NM, FILE_SAS_F_ID, FILE_SAS_F_LOC,
                                    FILE_SAS_F_NM, FILE_SAS_STP, FILE_SAS_STP_NM, FILE_LN_NUM, FILE_SAS_INP_LIB,
                                    FILE_SAS_INP_TBL, FILE_SAS_INP_FIL_NM, FILE_SAS_INP_ROW_RD, FILE_SAS_OUT_LIB,
                                    FILE_SAS_OUT_TBL, FILE_SAS_ROW_WRT, FILE_SAS_INP_MUL_FLG, FILE_SAS_INP_MUL_TBLS,
                                    FILE_SAS_MACRO_FLG, FILE_SAS_EXT_DB, FILE_EXC_DT, FILE_SAS_EXC_TM,
                                    FILE_SAS_EXC_CPU_TM, FILE_SAS_EXC_RL_TM, FILE_SAS_PROC_CAT, FILE_SAS_PROC_PROD,
                                    FILE_SAS_MIGR_DISP, FILE_SAS_MIGR_RUL_ID, FILE_SAS_MIGR_RUL, FILE_SAS_MIGR_REC_ACT,
                                    FILE_SAS_PROC_INMEM_FLG,
                                    FILE_SAS_PROC_ELT_FLG, FILE_SAS_PROC_GRID_FLG, FILE_SAS_PROC_INDB_FLG,
                                    FILE_SAS_SRC_TYP, FILE_SAS_ENV_NAME]
                # update a row of record to the given dataframe 'log_df'
                log_df = save_record_to_df(log_df, extracted_record)

                # Data initialization
                FILE_SAS_OUT_LIB = FILE_SAS_OUT_TBL = ""
                FILE_SAS_INP_LIB = FILE_SAS_INP_TBL = ""
                FILE_SAS_ROW_WRT = FILE_SAS_INP_ROW_RD = 0
    # save dateframe to xlsx file
    save_df_to_xlsx(log_df)

logging.info('end of the program')
