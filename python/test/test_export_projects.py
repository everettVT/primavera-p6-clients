# coding: utf-8

"""
    P6 EPPM Rest API

    The Primavera P6 Enterprise Project Portfolio Management (P6 EPPM) API is a flexible interface to P6 EPPM functionality based on the Representational State Transfer (REST) architectural style. Clients can use HTTP enabled technologies to interact with the API and access application features. For example, you can write programs in Javascript, Java, and other languages to create users, view a list of users, update a user's status, or update user details.

    The version of the OpenAPI document: 2022.12.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.export_projects import ExportProjects

class TestExportProjects(unittest.TestCase):
    """ExportProjects unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExportProjects:
        """Test ExportProjects
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExportProjects`
        """
        model = ExportProjects()
        if include_optional:
            return ExportProjects(
                encoding = '',
                file_type = 'GZIP',
                line_separator = 'WINDOWS',
                project_object_id = [
                    56
                    ],
                spread_period_type = 'HOUR',
                spacing = '',
                business_object_options = openapi_client.models.business_object_options.BusinessObjectOptions(
                    activity = openapi_client.models.activity.Activity(
                        include = True, 
                        field = [
                            'ACCOUNTING_VARIANCE'
                            ], ), 
                    activity_code = openapi_client.models.activity_code_export.ActivityCodeExport(
                        include = True, ), 
                    activity_code_assignment = openapi_client.models.activity_code_assignment.ActivityCodeAssignment(
                        include = True, ), 
                    activity_code_type = openapi_client.models.activity.Activity(
                        include = True, ), 
                    activity_expense = openapi_client.models.activity_expense.ActivityExpense(
                        include = True, ), 
                    activity_note = openapi_client.models.activity_note.ActivityNote(
                        include = True, ), 
                    activity_period_actual = openapi_client.models.activity_period_actual.ActivityPeriodActual(
                        include = True, ), 
                    activity_risk = openapi_client.models.activity_risk.ActivityRisk(
                        include = True, ), 
                    activity_step = openapi_client.models.activity_step.ActivityStep(
                        include = True, ), 
                    calendar = openapi_client.models.calendar.Calendar(
                        include = True, ), 
                    cost_account = openapi_client.models.cost_account.CostAccount(
                        include = True, ), 
                    currency = openapi_client.models.currency.Currency(
                        include = True, ), 
                    document = openapi_client.models.document.Document(
                        include = True, ), 
                    document_category = openapi_client.models.document_category.DocumentCategory(
                        include = True, ), 
                    document_status_code = openapi_client.models.document_status_code.DocumentStatusCode(
                        include = True, ), 
                    eps = openapi_client.models.eps.EPS(
                        include = True, ), 
                    expense_category = openapi_client.models.expense_category.ExpenseCategory(
                        include = True, ), 
                    financial_period = openapi_client.models.financial_period.FinancialPeriod(
                        include = True, ), 
                    funding_source = openapi_client.models.funding_source.FundingSource(
                        include = True, ), 
                    notebook_topic = openapi_client.models.notebook_topic.NotebookTopic(
                        include = True, ), 
                    obs = openapi_client.models.obs.OBS(
                        include = True, ), 
                    project = openapi_client.models.project.Project(
                        include = True, ), 
                    project_budget_change_log = openapi_client.models.project_budget_change_log.ProjectBudgetChangeLog(
                        include = True, ), 
                    project_code = openapi_client.models.project_code.ProjectCode(
                        include = True, ), 
                    project_code_assignment = openapi_client.models.project_code_assignment.ProjectCodeAssignment(
                        include = True, ), 
                    project_code_type = openapi_client.models.project_code_type.ProjectCodeType(
                        include = True, ), 
                    project_document = openapi_client.models.project_document.ProjectDocument(
                        include = True, ), 
                    project_funding = openapi_client.models.project_funding.ProjectFunding(
                        include = True, ), 
                    project_issue = openapi_client.models.project_issue.ProjectIssue(
                        include = True, ), 
                    project_note = openapi_client.models.project_note.ProjectNote(
                        include = True, ), 
                    project_resource = openapi_client.models.project_resource.ProjectResource(
                        include = True, ), 
                    project_resource_category = openapi_client.models.project_resource_category.ProjectResourceCategory(
                        include = True, ), 
                    project_resource_quantity = openapi_client.models.project_resource_quantity.ProjectResourceQuantity(
                        include = True, ), 
                    project_spending_plan = openapi_client.models.project_spending_plan.ProjectSpendingPlan(
                        include = True, ), 
                    project_threshold = openapi_client.models.project_threshold.ProjectThreshold(
                        include = True, ), 
                    relationship = openapi_client.models.relationship.Relationship(
                        include = True, ), 
                    resource = openapi_client.models.resource.Resource(
                        include = True, ), 
                    resource_assignment = openapi_client.models.resource_assignment.ResourceAssignment(
                        include = True, ), 
                    resource_assignment_period_actual = openapi_client.models.resource_assignment_period_actual.ResourceAssignmentPeriodActual(
                        include = True, ), 
                    resource_code = openapi_client.models.resource_code.ResourceCode(
                        include = True, ), 
                    resource_code_assignment = openapi_client.models.resource_code_assignment.ResourceCodeAssignment(
                        include = True, ), 
                    resource_code_type = openapi_client.models.resource_code_type.ResourceCodeType(
                        include = True, ), 
                    role_code = openapi_client.models.role_code.RoleCode(
                        include = True, ), 
                    role_code_assignment = openapi_client.models.role_code_assignment.RoleCodeAssignment(
                        include = True, ), 
                    role_code_type = openapi_client.models.role_code_type.RoleCodeType(
                        include = True, ), 
                    resource_curve = openapi_client.models.resource_curve.ResourceCurve(
                        include = True, ), 
                    resource_rate = openapi_client.models.resource_rate.ResourceRate(
                        include = True, ), 
                    resource_role = openapi_client.models.resource_role.ResourceRole(
                        include = True, ), 
                    risk = openapi_client.models.risk.Risk(
                        include = True, ), 
                    risk_category = openapi_client.models.risk_category.RiskCategory(
                        include = True, ), 
                    risk_impact = openapi_client.models.risk_impact.RiskImpact(
                        include = True, ), 
                    risk_matrix_score = openapi_client.models.risk_matrix_score.RiskMatrixScore(
                        include = True, ), 
                    risk_matrix_threshold = openapi_client.models.risk_matrix_threshold.RiskMatrixThreshold(
                        include = True, ), 
                    risk_response_action = openapi_client.models.risk_response_action.RiskResponseAction(
                        include = True, ), 
                    risk_response_action_impact = openapi_client.models.risk_response_action_impact.RiskResponseActionImpact(
                        include = True, ), 
                    risk_response_plan = openapi_client.models.risk_response_plan.RiskResponsePlan(
                        include = True, ), 
                    risk_matrix = openapi_client.models.risk_matrix.RiskMatrix(
                        include = True, ), 
                    risk_threshold_level = openapi_client.models.risk_threshold_level.RiskThresholdLevel(
                        include = True, ), 
                    risk_threshold = openapi_client.models.risk_threshold.RiskThreshold(
                        include = True, ), 
                    role = openapi_client.models.role.Role(
                        include = True, ), 
                    role_rate = openapi_client.models.role_rate.RoleRate(
                        include = True, ), 
                    role_limit = openapi_client.models.role_limit.RoleLimit(
                        include = True, ), 
                    shift = openapi_client.models.shift.Shift(
                        include = True, ), 
                    threshold_parameter = openapi_client.models.threshold_parameter.ThresholdParameter(
                        include = True, ), 
                    udf_code = openapi_client.models.udf_code.UDFCode(
                        include = True, ), 
                    udf_type = openapi_client.models.udf_type.UDFType(
                        include = True, ), 
                    udf_value = openapi_client.models.udf_value.UDFValue(
                        include = True, ), 
                    unit_of_measure = openapi_client.models.unit_of_measure.UnitOfMeasure(
                        include = True, ), 
                    wbs = openapi_client.models.wbs.WBS(
                        include = True, ), 
                    wbs_category = openapi_client.models.wbs_category.WBSCategory(
                        include = True, ), 
                    wbs_milestone = openapi_client.models.wbs_milestone.WBSMilestone(
                        include = True, ), )
            )
        else:
            return ExportProjects(
        )
        """

    def testExportProjects(self):
        """Test ExportProjects"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
