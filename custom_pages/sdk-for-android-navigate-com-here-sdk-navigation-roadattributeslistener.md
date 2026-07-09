---
title: "RoadAttributesListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-roadattributeslistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">RoadAttributesListener</span>

</div>

<div class="block">

This interface should be implemented in order to receive attributes of the current road.

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

      onRoadAttributesUpdated ( RoadAttributes roadAttributes)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called whenever any attribute of the current road changes.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onRoadAttributesUpdated-com-here-sdk-navigation-RoadAttributes" class="section detail">

    ### onRoadAttributesUpdated

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onRoadAttributesUpdated</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadattributes" title="class in com.here.sdk.navigation">RoadAttributes</a> roadAttributes)</span>

    </div>

    <div class="block">

    Called whenever any attribute of the current road changes. It's guaranteed to be called at least once for the first road the user is traveling on.

    </div>

    Parameters:  
    `roadAttributes` -

    The object that contains attributes of the current road.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

