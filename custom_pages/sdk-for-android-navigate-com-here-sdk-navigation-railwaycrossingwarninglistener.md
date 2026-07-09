---
title: "RailwayCrossingWarningListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-railwaycrossingwarninglistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">RailwayCrossingWarningListener</span>

</div>

<div class="block">

This interface should be implemented in order to receive railway crossing warnings. Note: The railway crossing warner can be either a zone warner or a point warner, depending on whether the railroad crossing warning is given for a railroad crossing zone or just a point. This means that for a railway crossing there will can be either 2 or 3 warnings emitted. In case the railroad crossing is a zone warner then 3 warnings will be emitted with the RailwayCrossingWarning.distance_type set to DistanceType.AHEAD , DistanceType.REACHED and lastly DistanceType.PASSED when the end of the railway crossing is passed. In case the railroad crossing is a point warner then 2 warnings will be emitted with the RailwayCrossingWarning.distance_type set to DistanceType.AHEAD and DistanceType.PASSED when the end of the railway crossing is passed.

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

      onRailwayCrossingWarningUpdated ( RailwayCrossingWarning railwayCrossingWarning)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called whenever a new railway crossing warning is available.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onRailwayCrossingWarningUpdated-com-here-sdk-navigation-RailwayCrossingWarning" class="section detail">

    ### onRailwayCrossingWarningUpdated

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onRailwayCrossingWarningUpdated</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-railwaycrossingwarning" title="class in com.here.sdk.navigation">RailwayCrossingWarning</a> railwayCrossingWarning)</span>

    </div>

    <div class="block">

    Called whenever a new railway crossing warning is available.

    </div>

    Parameters:  
    `railwayCrossingWarning` -

    The object that contains details on the railway crossing warning.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

