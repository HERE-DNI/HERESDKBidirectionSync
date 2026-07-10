---
title: "RoadTextsListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-roadtextslistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">RoadTextsListener</span>

</div>

<div class="block">

This interface should be implemented in order to receive textual attributes of the current road.

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

      onRoadTextsUpdated ( RoadTexts roadTexts)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called whenever any textual attribute of the current road changes, i.e., the current road texts differs from the previous one already issued.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onRoadTextsUpdated-com-here-sdk-routing-RoadTexts" class="section detail">

    ### onRoadTextsUpdated

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onRoadTextsUpdated</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-roadtexts" title="class in com.here.sdk.routing">RoadTexts</a> roadTexts)</span>

    </div>

    <div class="block">

    Called whenever any textual attribute of the current road changes, i.e., the current road texts differs from the previous one already issued.

    </div>

    Parameters:  
    `roadTexts` -

    The object that contains the textual attributes of the current road.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

