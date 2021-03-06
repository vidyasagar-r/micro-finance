from django.conf.urls import url
from micro_admin.views import *

urlpatterns = [

    url(r'^$', index, name='microadmin_index'),
    url(r'^login/$', user_login, name='login'),
    url(r'^createbranch/$', create_branch, name='createbranch'),
    url(r'^createclient/$', create_client, name='createclient'),
    url(r'^createuser/$', create_user, name='createuser'),
    url(r'^creategroup/$', create_group, name='creategroup'),
    url(r'^editbranch/(?P<branch_id>\d+)/$', edit_branch, name='editbranch'),
    url(r'^edituser/(?P<user_id>\d+)/$', edit_user, name='edituser'),
    url(r'^editclient/(?P<client_id>\d+)/$', edit_client, name='editclient'),
    url(r'^branchprofile/(?P<branch_id>\d+)/$',
        branch_profile, name='branchprofile'),
    url(r'^userprofile/(?P<user_id>\d+)/$',
        user_profile, name='userprofile'),
    url(r'^clientprofile/(?P<client_id>\d+)/$',
        client_profile, name='clientprofile'),
    url(r'^groupprofile/(?P<group_id>\d+)/$',
        group_profile, name='groupprofile'),
    url(r'^userslist/$', users_list, name='userslist'),
    url(r'^viewbranch/$', view_branch, name='viewbranch'),
    url(r'^groupslist/$', groups_list, name='groupslist'),
    url(r'^viewclient/$', view_client, name='viewclient'),
    url(r'^deletebranch/(?P<branch_id>\d+)/$',
        delete_branch, name='deletebranch'),
    url(r'^deleteuser/(?P<user_id>\d+)/$', delete_user, name='deleteuser'),
    url(r'^deletegroup/(?P<group_id>\d+)/$', delete_group, name='deletegroup'),
    url(r'^deleteclient/(?P<client_id>\d+)/$',
        delete_client, name='deleteclient'),
    url(r'^assignstaff/(?P<group_id>\d+)/$',
        assign_staff_to_group, name='assignstaff'),
    url(r'^addmember/(?P<group_id>\d+)/$',
        addmembers_to_group, name='addmember'),
    url(r'^viewmembers/(?P<group_id>\d+)/$',
        viewmembers_under_group, name='viewmembers'),
    url(r'^removemember/(?P<group_id>\d+)/(?P<client_id>\d+)/$',
        removemembers_from_group, name='removemember'),
    url(r'^updateclientprofile/(?P<client_id>\d+)/$',
        update_clientprofile, name='updateclientprofile'),
    url(r'^groupmeetings/(?P<group_id>\d+)/$',
        group_meetings, name='groupmeetings'),
    url(r'^addgroupmeeting/(?P<group_id>\d+)/$',
        add_group_meeting, name='addgroupmeeting'),
    url(r'^clientsavingsapplication/(?P<client_id>\d+)/$',
        client_savings_application, name='clientsavingsapplication'),
    url(r'^clientsavingsaccount/(?P<client_id>\d+)/$',
        client_savings_account, name='clientsavingsaccount'),
    url(r'^groupsavingsapplication/(?P<group_id>\d+)/$',
        group_savings_application, name='groupsavingsapplication'),
    url(r'^groupsavingsaccount/(?P<group_id>\d+)/$',
        group_savings_account, name='groupsavingsaccount'),
    # savings account status
    url(r'^savings-account/status/(?P<savingsaccount_id>\d+)/$',
        change_savings_account_status, name='savings_account_status'),

    url(r'^viewgroupsavingsdeposits/(?P<group_id>\d+)/$',
        view_groupsavings_deposits, name='viewgroupsavingsdeposits'),
    url(r'^viewgroupsavingswithdrawals/(?P<group_id>\d+)/$',
        view_groupsavings_withdrawals, name='viewgroupsavingswithdrawals'),
    url(r'^grouploanapplication/(?P<group_id>\d+)/$',
        group_loan_application, name='grouploanapplication'),
    url(r'^grouploanaccount/(?P<loanaccount_id>\d+)/$',
        group_loan_account, name='grouploanaccount'),
    url(r'^clientloanapplication/(?P<client_id>\d+)/$',
        client_loan_application, name='clientloanapplication'),
    url(r'^clientloanaccount/(?P<loanaccount_id>\d+)/$',
        client_loan_account, name='clientloanaccount'),
    # Loan account status
    url(r'^loan-account/status/(?P<loanaccount_id>\d+)/$',
        change_loan_account_status, name='change_loan_account_status'),

    url(r'^listofclientloandeposits/(?P<client_id>\d+)/(?P<loanaccount_id>\d+)/$',
        listofclient_loan_deposits, name='listofclientloandeposits'),
    url(r'^listofclientsavingsdeposits/(?P<client_id>\d+)/$',
        listofclient_savings_deposits, name='listofclientsavingsdeposits'),
    url(r'^listofclientsavingswithdrawals/(?P<client_id>\d+)/$',
        listofclient_savings_withdrawals,
        name='listofclientsavingswithdrawals'),
    url(r'^viewgrouploandeposits/(?P<group_id>\d+)/(?P<loanaccount_id>\d+)/$',
        view_grouploan_deposits, name='viewgrouploandeposits'),
    url(r'^issueloan/(?P<loanaccount_id>\d+)/$', issue_loan, name='issueloan'),
    url(r'^receiptsdeposit/$', receipts_deposit, name="receiptsdeposit"),
    url(r'^receiptslist/$', receipts_list, name="receiptslist"),
    url(r'^ledgeraccount/(?P<client_id>\d+)/(?P<loanaccount_id>\d+)/$',
        ledger_account, name="ledgeraccount"),
    url(r'^generalledger/$', general_ledger, name="generalledger"),
    url(r'^fixeddeposits/$', fixed_deposits, name="fixeddeposits"),
    url(r'^clientfixeddepositsprofile/(?P<fixed_deposit_id>\d+)/$',
        client_fixed_deposits_profile, name="clientfixeddepositsprofile"),
    url(r'^viewclientfixeddeposits/$',
        view_client_fixed_deposits, name="viewclientfixeddeposits"),
    url(r'^viewdaybook/$', view_day_book, name="viewdaybook"),
    url(r'^viewparticularclientfixeddeposits/(?P<client_id>\d+)/$',
        view_particular_client_fixed_deposits,
        name="viewparticularclientfixeddeposits"),
    url(r'^payslip/$', pay_slip, name="payslip"),
    url(r'^grouploanaccountslist/(?P<group_id>\d+)/$',
        view_group_loanslist, name="grouploanaccountslist"),
    url(r'^clientloanaccountslist/(?P<client_id>\d+)/$',
        view_client_loanslist, name="clientloanaccountslist"),
    url(r'^paymentslist/$', payments_list, name="paymentslist"),
    url(r'^recurringdeposits/$', recurring_deposits, name="recurringdeposits"),
    url(r'^clientrecurringdepositsprofile/(?P<recurring_deposit_id>\d+)/$',
        client_recurring_deposits_profile,
        name="clientrecurringdepositsprofile"),
    url(r'^viewclientrecurringdeposits/$', view_client_recurring_deposits,
        name="viewclientrecurringdeposits"),
    url(r'^viewparticularclientrecurringdeposits/(?P<client_id>\d+)/$',
        view_particular_client_recurring_deposits,
        name="viewparticularclientrecurringdeposits"),
    url(r'^logout/$', user_logout, name="logout"),
    url(r'^clientledgercsvdownload/(?P<client_id>\d+)/$',
        clientledger_csvdownload, name="clientledgercsvdownload"),
    url(r'^clientledgerexceldownload/(?P<client_id>\d+)/$',
        clientledger_exceldownload, name="clientledgerexceldownload"),
    url(r'^clientledgerpdfdownload/(?P<client_id>\d+)/$',
        clientledger_pdfdownload, name="clientledgerpdfdownload"),
    url(r'^generalledgerpdfdownload/$', general_ledger_pdfdownload,
        name="generalledgerpdfdownload"),
    url(r'^daybookpdfdownload/(?P<date>\d{4}-\d{2}-\d{2})/$',
        daybook_pdfdownload, name="daybookpdfdownload"),
    url(r'^userchangepassword/(?P<user_id>\d+)/$', user_change_password,
        name="userchangepassword"),
    url(r'^getmemberloanaccounts/$', getmember_loanaccounts,
        name="getmemberloanaccounts"),
    url(r'^getloandemands/$', getloan_demands, name="getloandemands"),
]