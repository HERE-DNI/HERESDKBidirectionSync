---
title: "RouteDeviationListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-routedeviationlistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">RouteDeviationListener</span>

</div>

<div class="block">

This interface should be implemented in order to receive notifications about route deviations from Navigator .

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

      onRouteDeviation ( RouteDeviation routeDeviation)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called whenever route deviation has been observed.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onRouteDeviation-com-here-sdk-navigation-RouteDeviation" class="section detail">

    ### onRouteDeviation

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onRouteDeviation</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-routedeviation" title="class in com.here.sdk.navigation">RouteDeviation</a> routeDeviation)</span>

    </div>

    <div class="block">

    Called whenever route deviation has been observed. It contains the information that can be used to decide whether to request a re-route calculation from the routing engine.

    </div>

    Parameters:  
    `routeDeviation` -

    The route deviation observed.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

