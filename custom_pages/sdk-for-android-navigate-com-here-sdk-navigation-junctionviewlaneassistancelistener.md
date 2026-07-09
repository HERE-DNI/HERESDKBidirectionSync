---
title: "JunctionViewLaneAssistanceListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-junctionviewlaneassistancelistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">JunctionViewLaneAssistanceListener</span>

</div>

<div class="block">

This interface should be implemented in order to receive notifications on JunctionViewLaneAssistance . See JunctionViewLaneAssistance documentation for further details.

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

      onLaneAssistanceUpdated ( JunctionViewLaneAssistance laneAssistance)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called before and after a complex junction if lane recommendations are available.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onLaneAssistanceUpdated-com-here-sdk-navigation-JunctionViewLaneAssistance" class="section detail">

    ### onLaneAssistanceUpdated

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onLaneAssistanceUpdated</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-junctionviewlaneassistance" title="class in com.here.sdk.navigation">JunctionViewLaneAssistance</a> laneAssistance)</span>

    </div>

    <div class="block">

    Called before and after a complex junction if lane recommendations are available.

    </div>

    Parameters:  
    `laneAssistance` -

    The <a href="sdk-for-android-navigate-com-here-sdk-navigation-junctionviewlaneassistance" title="class in com.here.sdk.navigation">`JunctionViewLaneAssistance`</a> notification.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

