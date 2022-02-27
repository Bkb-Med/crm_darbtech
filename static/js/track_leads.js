odoo.define("crm_darbtech.leadsTrack", function (require) {
  "use strict";
  var core = require("web.core");
  var QWeb = core.qweb;
  var Widget = require("web.Widget");
  var SystrayMenu = require("web.SystrayMenu");
 
  var LeadWidget = Widget.extend({
    name: "lead_widget",
    template: "crm_darbtech.leadsTrack",
    events: {
       "show.bs.dropdown": "leadWidget_Update",
    },
    
    start: function () {
      this._$leadsPreview = this.$(".o_mail_systray_dropdown_items");
      this.counter_Update();
      this.leadWidget_Update();
      return this._super();
    },
    
    counter_Update: function (data) {
      if (data) {
        if (data.lead_created) {
          this.Counter++;
        }
        if (data.lead_deleted && this.Counter > 0) {
          this.Counter--;
        }
       
      }
    },
    data_Get: function () {
      var that = this;

      return that
        ._rpc({
          model: "res.users",
          method: "getLeads",

        })
        .then(function (data) {
          that.leads = data;
          that.Counter = _.reduce(
            data,
            function (total, previous_data) {
              return total + previous_data.total;
            },
            0
          );
          
        });
    },
    
    
    leadWidget_Update: function () {
      var that = this;
      that.data_Get().then(function () {
        that._$leadsPreview.html(
          QWeb.render("mail.systray.LeadWidget.Previews", {
            leads: that.leads,
          })
        );
      });
    },
    
  

   
   
  });
  LeadWidget.prototype.sequence = 100;
  SystrayMenu.Items.push(LeadWidget);
  return LeadWidget;
});
