---
title: "MilestoneStatusListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-milestonestatuslistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">MilestoneStatusListener</span>

</div>

<div class="block">

This interface should be implemented in order to receive notifications from this class about the arrival at each Milestone or missing it.

</div>

</div>

- <div id="sdk-for-android-navigate-method-summary" class="section method-summary">

  <div id="sdk-for-android-navigate-method-summary-table">

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Method

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      onMilestoneStatusUpdated ( Milestone milestone, MilestoneStatus status)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called when a milestone status has been changed.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onMilestoneStatusUpdated-com-here-sdk-navigation-Milestone-com-here-sdk-navigation-MilestoneStatus" class="section detail">

    ### onMilestoneStatusUpdated

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onMilestoneStatusUpdated</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-milestone" title="class in com.here.sdk.navigation">Milestone</a> milestone, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-milestonestatus" title="enum class in com.here.sdk.navigation">MilestoneStatus</a> status)</span>

    </div>

    <div class="block">

    Called when a milestone status has been changed.

    </div>

    Parameters:  
    `milestone` -

    The reference to the <a href="sdk-for-android-navigate-com-here-sdk-navigation-milestone" title="class in com.here.sdk.navigation">`Milestone`</a>.

    `status` -

    The status of the <a href="sdk-for-android-navigate-com-here-sdk-navigation-milestone" title="class in com.here.sdk.navigation">`Milestone`</a>.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

