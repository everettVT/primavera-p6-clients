# coding: utf-8

"""
    P6 EPPM Rest API

    The Primavera P6 Enterprise Project Portfolio Management (P6 EPPM) API is a flexible interface to P6 EPPM functionality based on the Representational State Transfer (REST) architectural style. Clients can use HTTP enabled technologies to interact with the API and access application features. For example, you can write programs in Javascript, Java, and other languages to create users, view a list of users, update a user's status, or update user details.

    The version of the OpenAPI document: 2022.12.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.project import Project

class TestProject(unittest.TestCase):
    """Project unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Project:
        """Test Project
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Project`
        """
        model = Project()
        if include_optional:
            return Project(
                activity_default_activity_type = '',
                activity_default_calendar_name = '',
                activity_default_calendar_object_id = 56,
                activity_default_cost_account_object_id = 56,
                activity_default_duration_type = '',
                activity_default_percent_complete_type = '',
                activity_default_price_per_unit = 1.337,
                activity_default_review_required = True,
                activity_id_based_on_selected_activity = True,
                activity_id_increment = 56,
                activity_id_prefix = '',
                activity_id_suffix = 56,
                activity_percent_complete_based_on_activity_steps = True,
                add_actual_to_remaining = True,
                added_by = '',
                allow_negative_actual_units_flag = True,
                allow_status_review = True,
                annual_discount_rate = 1.337,
                anticipated_finish_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                anticipated_start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                assignment_default_driving_flag = True,
                assignment_default_rate_type = '',
                calculate_float_based_on_finish_date = True,
                check_out_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                check_out_status = True,
                check_out_user_object_id = 56,
                compute_total_float_type = '',
                contains_summary_data = True,
                contract_management_group_name = '',
                contract_management_project_name = '',
                cost_quantity_recalculate_flag = True,
                create_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                create_user = '',
                critical_activity_float_limit = 1.337,
                critical_activity_float_threshold = 1.337,
                critical_activity_path_type = '',
                critical_float_threshold = 1.337,
                current_baseline_project_object_id = 56,
                current_budget = 1.337,
                current_variance = 1.337,
                data_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                date_added = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                default_price_time_units = '',
                description = '',
                discount_application_period = '',
                distributed_current_budget = 1.337,
                earned_value_compute_type = '',
                earned_value_etc_compute_type = '',
                earned_value_etc_user_value = 1.337,
                earned_value_user_percent = 1.337,
                enable_prime_syc_flag = True,
                enable_publication = True,
                enable_summarization = True,
                etl_interval = '',
                financial_period_template_id = 56,
                finish_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                fiscal_year_start_month = 56,
                forecast_finish_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                forecast_start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                guid = '',
                has_future_bucket_data = True,
                history_interval = '',
                history_level = '',
                id = '',
                ignore_other_project_relationships = True,
                independent_etc_labor_units = 1.337,
                independent_etc_total_cost = 1.337,
                integrated_type = '',
                is_template = True,
                last_apply_actuals_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_financial_period_object_id = 56,
                last_level_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_published_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_schedule_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_summarized_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_update_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_update_user = '',
                latitude = 1.337,
                level_all_resources = True,
                level_date_flag = True,
                level_float_threshold_count = 56,
                level_outer_assign = True,
                level_outer_assign_priority = 56,
                level_over_allocation_percent = 1.337,
                level_priority_list = '',
                level_resource_list = '',
                level_within_float = True,
                leveling_priority = 56,
                limit_multiple_float_paths = True,
                link_actual_to_actual_this_period = True,
                link_percent_complete_with_actual = True,
                link_planned_and_at_completion_flag = True,
                location_name = '',
                location_object_id = 56,
                longitude = 1.337,
                make_open_ended_activities_critical = True,
                maximum_multiple_float_paths = 56,
                multiple_float_paths_enabled = True,
                multiple_float_paths_ending_activity_object_id = 56,
                multiple_float_paths_use_total_float = True,
                must_finish_by_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '',
                net_present_value = 1.337,
                obs_name = '',
                obs_object_id = 56,
                object_id = 56,
                original_budget = 1.337,
                out_of_sequence_schedule_type = '',
                overall_project_score = 56,
                owner_resource_object_id = 56,
                parent_epsid = '',
                parent_eps_name = '',
                parent_eps_object_id = 56,
                payback_period = 56,
                performance_percent_complete_by_labor_units = 1.337,
                planned_start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                post_response_pessimistic_finish = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                post_response_pessimistic_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                pre_response_pessimistic_finish = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                pre_response_pessimistic_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                primary_resources_can_mark_activities_as_completed = True,
                primary_resources_can_update_activity_dates = True,
                project_forecast_start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                project_schedule_type = '',
                property_type = '',
                proposed_budget = 1.337,
                publication_priority = 56,
                publish_level = '',
                relationship_lag_calendar = '',
                reset_planned_to_remaining_flag = True,
                resource_can_be_assigned_to_same_activity_more_than_once = True,
                resource_name = '',
                resources_can_assign_themselves_to_activities = True,
                resources_can_assign_themselves_to_activities_outside_obs_access = True,
                resources_can_edit_assignment_percent_complete = True,
                resources_can_mark_assignment_as_completed = True,
                resources_can_view_inactive_activities = True,
                return_on_investment = 1.337,
                review_type = '',
                risk_exposure = 1.337,
                risk_level = '',
                risk_matrix_name = '',
                risk_matrix_object_id = 56,
                risk_score = 56,
                schedule_wbs_hierarchy_type = '',
                scheduled_finish_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                source_project_object_id = 56,
                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                start_to_start_lag_calculation_type = True,
                status = '',
                status_reviewer_name = '',
                status_reviewer_object_id = '',
                strategic_priority = 56,
                summarize_resources_roles_by_wbs = True,
                summarize_to_wbs_level = 56,
                summarized_data_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                summary_accounting_variance_by_cost = 1.337,
                summary_accounting_variance_by_labor_units = 1.337,
                summary_activity_count = 56,
                summary_actual_duration = 1.337,
                summary_actual_expense_cost = 1.337,
                summary_actual_finish_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                summary_actual_labor_cost = 1.337,
                summary_actual_labor_units = 1.337,
                summary_actual_material_cost = 1.337,
                summary_actual_non_labor_cost = 1.337,
                summary_actual_non_labor_units = 1.337,
                summary_actual_start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                summary_actual_this_period_cost = 1.337,
                summary_actual_this_period_labor_cost = 1.337,
                summary_actual_this_period_labor_units = 1.337,
                summary_actual_this_period_material_cost = 1.337,
                summary_actual_this_period_non_labor_cost = 1.337,
                summary_actual_this_period_non_labor_units = 1.337,
                summary_actual_total_cost = 1.337,
                summary_actual_value_by_cost = 1.337,
                summary_actual_value_by_labor_units = 1.337,
                summary_at_completion_duration = 1.337,
                summary_at_completion_expense_cost = 1.337,
                summary_at_completion_labor_cost = 1.337,
                summary_at_completion_labor_units = 1.337,
                summary_at_completion_material_cost = 1.337,
                summary_at_completion_non_labor_cost = 1.337,
                summary_at_completion_non_labor_units = 1.337,
                summary_at_completion_total_cost = 1.337,
                summary_at_completion_total_cost_variance = 1.337,
                summary_baseline_completed_activity_count = 56,
                summary_baseline_duration = 1.337,
                summary_baseline_expense_cost = 1.337,
                summary_baseline_finish_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                summary_baseline_in_progress_activity_count = 56,
                summary_baseline_labor_cost = 1.337,
                summary_baseline_labor_units = 1.337,
                summary_baseline_material_cost = 1.337,
                summary_baseline_non_labor_cost = 1.337,
                summary_baseline_non_labor_units = 1.337,
                summary_baseline_not_started_activity_count = 56,
                summary_baseline_start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                summary_baseline_total_cost = 1.337,
                summary_budget_at_completion_by_cost = 1.337,
                summary_budget_at_completion_by_labor_units = 1.337,
                summary_completed_activity_count = 56,
                summary_cost_percent_complete = 1.337,
                summary_cost_percent_of_planned = 1.337,
                summary_cost_performance_index_by_cost = 1.337,
                summary_cost_performance_index_by_labor_units = 1.337,
                summary_cost_variance_by_cost = 1.337,
                summary_cost_variance_by_labor_units = 1.337,
                summary_cost_variance_index = 1.337,
                summary_cost_variance_index_by_cost = 1.337,
                summary_cost_variance_index_by_labor_units = 1.337,
                summary_duration_percent_complete = 1.337,
                summary_duration_percent_of_planned = 1.337,
                summary_duration_variance = 1.337,
                summary_earned_value_by_cost = 1.337,
                summary_earned_value_by_labor_units = 1.337,
                summary_estimate_at_completion_by_cost = 1.337,
                summary_estimate_at_completion_by_labor_units = 1.337,
                summary_estimate_at_completion_high_percent_by_labor_units = 1.337,
                summary_estimate_at_completion_low_percent_by_labor_units = 1.337,
                summary_estimate_to_complete_by_cost = 1.337,
                summary_estimate_to_complete_by_labor_units = 1.337,
                summary_expense_cost_percent_complete = 1.337,
                summary_expense_cost_variance = 1.337,
                summary_finish_date_variance = 1.337,
                summary_in_progress_activity_count = 56,
                summary_labor_cost_percent_complete = 1.337,
                summary_labor_cost_variance = 1.337,
                summary_labor_units_percent_complete = 1.337,
                summary_labor_units_variance = 1.337,
                summary_level = '',
                summary_material_cost_percent_complete = 1.337,
                summary_material_cost_variance = 1.337,
                summary_non_labor_cost_percent_complete = 1.337,
                summary_non_labor_cost_variance = 1.337,
                summary_non_labor_units_percent_complete = 1.337,
                summary_non_labor_units_variance = 1.337,
                summary_not_started_activity_count = 56,
                summary_performance_percent_complete_by_cost = 1.337,
                summary_performance_percent_complete_by_labor_units = 1.337,
                summary_planned_cost = 1.337,
                summary_planned_duration = 1.337,
                summary_planned_expense_cost = 1.337,
                summary_planned_finish_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                summary_planned_labor_cost = 1.337,
                summary_planned_labor_units = 1.337,
                summary_planned_material_cost = 1.337,
                summary_planned_non_labor_cost = 1.337,
                summary_planned_non_labor_units = 1.337,
                summary_planned_start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                summary_planned_value_by_cost = 1.337,
                summary_planned_value_by_labor_units = 1.337,
                summary_progress_finish_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                summary_remaining_duration = 1.337,
                summary_remaining_expense_cost = 1.337,
                summary_remaining_finish_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                summary_remaining_labor_cost = 1.337,
                summary_remaining_labor_units = 1.337,
                summary_remaining_material_cost = 1.337,
                summary_remaining_non_labor_cost = 1.337,
                summary_remaining_non_labor_units = 1.337,
                summary_remaining_start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                summary_remaining_total_cost = 1.337,
                summary_schedule_percent_complete = 1.337,
                summary_schedule_percent_complete_by_labor_units = 1.337,
                summary_schedule_performance_index_by_cost = 1.337,
                summary_schedule_performance_index_by_labor_units = 1.337,
                summary_schedule_variance_by_cost = 1.337,
                summary_schedule_variance_by_labor_units = 1.337,
                summary_schedule_variance_index = 1.337,
                summary_schedule_variance_index_by_cost = 1.337,
                summary_schedule_variance_index_by_labor_units = 1.337,
                summary_start_date_variance = 1.337,
                summary_to_complete_performance_index_by_cost = 1.337,
                summary_total_cost_variance = 1.337,
                summary_total_float = 1.337,
                summary_units_percent_complete = 1.337,
                summary_variance_at_completion_by_labor_units = 1.337,
                sync_wbs_hierarchy_flag = True,
                team_member_activity_fields = '',
                team_member_add_new_actual_units = True,
                team_member_assignment_option = '',
                team_member_can_status_other_resources = True,
                team_member_can_update_notebooks = True,
                team_member_display_baseline_dates_flag = True,
                team_member_display_planned_units = True,
                team_member_display_total_float_flag = True,
                team_member_include_primary_resources = True,
                team_member_read_only_activity_fields = '',
                team_member_resource_assignment_fields = '',
                team_member_step_udf_viewable_fields = '',
                team_member_steps_add_deletable = True,
                team_member_viewable_fields = '',
                total_benefit_plan = 1.337,
                total_benefit_plan_tally = 1.337,
                total_funding = 1.337,
                total_spending_plan = 1.337,
                total_spending_plan_tally = 1.337,
                unallocated_budget = 1.337,
                undistributed_current_variance = 1.337,
                unifier_cbs_tasks_only_flag = True,
                unifier_data_mapping_name = '',
                unifier_delete_activities_flag = True,
                unifier_enabled_flag = True,
                unifier_project_name = '',
                unifier_project_number = '',
                unifier_schedule_sheet_name = '',
                use_expected_finish_dates = True,
                use_project_baseline_for_earned_value = True,
                wbs_code_separator = '',
                wbs_hierarchy_levels = 56,
                wbs_milestone_percent_complete = 1.337,
                wbs_object_id = 56,
                web_site_root_directory = '',
                web_site_url = '',
                external = True
            )
        else:
            return Project(
                id = '',
                name = '',
                parent_eps_object_id = 56,
        )
        """

    def testProject(self):
        """Test Project"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
