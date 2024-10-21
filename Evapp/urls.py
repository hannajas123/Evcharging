from django.urls import path

from Evapp import views

urlpatterns=[


#############################################Admin##############################################################

    path('login/',views.login),
    path('login_post/',views.login_post),
    path('change_password/',views.change_password),
    path('change_pswd_post/',views.change_pswd_post),
    path('logout/',views.logout),
    path('Admin_home/',views.Admin_home),

    path('Add_category/',views.Add_category),
    path('add_cat_post/',views.Add_cate_post),
    path('View_category/',views.view_category),
    path('search_category/',views.search_category),
    path('editcategory/<did>',views.EditCategory),
    path('edit_cate_post/',views.edit_cate_post),
    path('Delete_category/<did>',views.Delete_category),

    path('manage_ev/',views.manage_evStations),
    path('search_Ev/',views.search_Ev),
    path('Approve_ev_statn/<did>',views.Approve_ev),
    path('approved_ev/',views.Approved_stations),
    path('Search_Apprved_ev/',views.Search_Apprved_ev),
    path('Reject_ev_statn/<did>',views.Reject_ev),
    path('rejected_ev/',views.RejectedStations),
    path('Search_Rjctd_ev/',views.Search_Rjctd_ev),

    path('manage_workers/',views.manage_workers),
    path('Search_workers/',views.Search_workers),
    path('verify_wrkr/<did>',views.verify_worker),
    path('verifyed_workers/',views.verifyed_workers),
    path('Search_vrfyd_workers/',views.Search_vrfyd_workers),
    path('Reject_wrkr/<did>',views.reject_worker),
    path('Rejeced_workers/',views.Rejected_workers),
    path('Search_Rjctd_workers/',views.Search_Rjctd_workers),

    path('view_users/',views.view_users),
    path('Search_User/',views.Search_User),

    path('view_feedback/',views.view_feedback),
    path('Search_Feedback/',views.Search_Feedback),

    path('view_user_complaint_nd_reply/',views.view_user_complaint_nd_reply),
    path('Search_User_comp/',views.Search_User_comp),
    path('send_user_reply/<did>',views.reply_user_com),
    path('send_usr_rply_post/',views.send_reply_post_user),
    path('view_workers_complaint_nd_reply/',views.view_worker_complaint_nd_reply),
    path('Search_Worker_comp/',views.Search_Worker_comp),
    path('send_worker_reply/<did>',views.reply_worker_com),
    path('send_wrkr_reply_post/',views.send_reply_post_worker),

    path('view_Station_complaint_nd_reply/',views.view_station_complaint_nd_reply),
    path('Search_Station_comp/',views.Search_staion_comp),
    path('send_Station_reply/<did>',views.reply_Station_com),
    path('send_Station_reply_post/',views.send_reply_post_station),
#######################################################EVstation##################################################

    path('Evstnhome/',views.home),

    path('signin/',views.signin),
    path('sigin_post_ev/',views.Signin_post),

    path('change_password_ev/',views.change_password_ev),
    path('change_pswd_post_ev/',views.change_pswd_post_ev),

    path('Addslot/',views.Addslot),
    path('Addslot_post/',views.Addslot_post),
    path('View_slot/',views.View_slot),
    path('Search_slots/',views.Search_slots),
    path('delete_slot/<did>',views.delete_slot),
    path('edit_slot/<did>',views.edit_slot),
    path('Edit_slot_post/',views.Edit_slot_post),

    path('view_slot_booked/',views.view_slot_booked),
    path('approve_slots/<did>',views.approve_slots),
    path('reject_slots/<did>',views.reject_slots),
    path('Search_booked_slots/',views.Search_booked_slots),
    path('View_Approved_slots/',views.View_Approved_slots),
    path('Approved_slot_search/',views.Approved_slot_search),
    path('View_Rejected_slots/',views.View_Rejected_slots),
    path('Rejected_slot_search/',views.Rejected_slot_search),

    path('View_users/',views.View_users),
    path('search_view_users/',views.search_view_users),

    path('Send_complaints/',views.Send_complaints),
    path('Send_comp_post/',views.Send_comp_post),
    path('View_reply/',views.View_reply),
    path('Search_View_reply/',views.Search_View_reply),

    path('View_general_feedback/',views.View_general_feedback),
    path('Search_general_feed/',views.Search_general_feed),
    path('view_user_feedback/',views.view_user_feedback),
    path('Search_user_feed/',views.Search_user_feed),
    ##########chat##########
    path('chat/<toid>',views.chat),
    path('chat_view/<tid>',views.chat_view),
    path('chat_send/<msg>/<tid>',views.chat_send),




#######################################################Worker#####################################################
   path('signupworker_post/',views.signupworker_post),

   path('login_worker_user_post/',views.login_worker_user_post),
   path('change_password_worker_post/',views.change_password_worker_post),

   path('add_service_post/',views.add_service_post),
   path('view_service_post/',views.view_service_post),
   path('edit_service_post/',views.edit_service_post),
   path('updaate_service_post/',views.updaate_service_post),
   path('delete_service_post/',views.delete_service_post),

   path('view_profile_post/',views.view_profile_post),
   path('update_workerprof/',views.update_workerprof),
   path('edit_profile_post/',views.edit_profile_post),

   path('view_servicebooking_post_ndverify/',views.view_servicebooking_post_ndverify),
   path('Approve_booking_post/',views.Approve_booking_post),
   path('Reject_booking_post/',views.Reject_booking_post),
   path('view_Approved_booking_post/',views.view_Approved_booking_post),
   path('view_rejected_booking_post/',views.view_rejected_booking_post),

   path('view_user_doubts_post/',views.view_user_doubts_post),
   path('send_reply_doubts_post/',views.send_reply_doubts_post),




#####################################################User#########################################################
   path('signup_user_post/',views.signup_user_post),
   path('change_password_user_post/',views.change_password_user_post),

   path('view_profile_user_post/',views.view_profile_user_post),
   path('update_User_profile/',views.update_User_profile),
   path('edit_profile_user_post/',views.edit_profile_user_post),

   path('view_service_user_post/',views.view_service_user_post),
   path('view_worker_nd_bookservice_user_post/',views.view_worker_nd_bookservice_user_post),
   path('User_view_workerService_post/',views.User_view_workerService_post),
   path('book_service_user_post/',views.book_service_user_post),

   path('view_worker_nd_service_status_user_post/',views.view_worker_nd_service_status_user_post),

   path('add_doubts_user_post/',views.add_doubts_user_post),
   path('view_solution_doubt_user_post/',views.view_solution_doubt_user_post),

   path('upload_post_user_post/',views.upload_post_user_post),
    path('view_USERS_post/',views.view_USERS_post),
   path('view_users_Post_user_post/',views.view_usersPOst_post),
   path('view_comments_user_post/',views.view_comments_user_post),
   path('view_other_user_post/',views.view_other_user_post),
   path('add_comments_others_post/',views.add_comments_others_post),

   path('view_ev_station_user_post/',views.view_ev_station_user_post),
    path('view_slots_of_ev_stations/',views.view_slots_of_ev_stations),
   path('bookslot_evstation_user_post/',views.bookslot_evstation_user_post),
   path('view_booking_status_user_post/',views.view_booking_status_user_post),

   path('send_complaints_user_post/',views.send_complaints_user_post),
   path('view_reply_user_post/',views.view_reply_user_post),

   path('send_feedback_about_evstation_user_post/',views.send_feedback_about_evstation_user_post),

    path('user_sendchat/',views.user_sendchat),
   path('user_viewchat/',views.user_viewchat),


]