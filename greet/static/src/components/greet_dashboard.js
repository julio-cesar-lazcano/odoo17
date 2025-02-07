/** @odoo-module **/

import { registry } from '@web/core/registry'
import { useService } from '@web/core/utils/hooks'
import { OwlChartRenderer } from './chart/chart_renderer'

const { Component, useState, onWillStart } = owl

class OwlGreetDashboard extends Component {
    setup() {
        this.orm = useService('orm')
        this.state = useState({ modules: [] });

        onWillStart(async () => {
            this.state.modules = await this.countGroupModules()
        });
    }
    async countGroupModules() {
    const countModules = await this.orm.searchRead(
      'ir.module.module',
      [["state", "=", "installed"]],
      ['id', 'icon', 'name']
    )

        console.log('countModules', countModules)

        return countModules
      }
}

OwlGreetDashboard.template = 'owl.OwlGreetDashboard'
OwlGreetDashboard.components = { OwlChartRenderer }

registry.category('actions').add('owl.greet_dashboard', OwlGreetDashboard)
