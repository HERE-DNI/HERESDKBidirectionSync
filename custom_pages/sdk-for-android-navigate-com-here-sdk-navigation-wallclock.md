---
title: "WallClock (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-wallclock"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">WallClock</span>

</div>

<div class="block">

Clock used to properly retrieve time-dependent data from the map.

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1">

  `static `<a href="sdk-for-android-navigate-com-here-sdk-navigation-wallclock" title="interface in com.here.sdk.navigation">`WallClock`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1">

      getDefault ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1">

  <div class="block">

  Provides the default WallClock implementation based on the device clock.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util"><code>Date</code></a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      now ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the current time from the device clock.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-now" class="section detail">

    ### now

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util">Date</a></span> <span class="element-name">now</span>()

    </div>

    <div class="block">

    Gets the current time from the device clock.

    </div>

    Returns:  
    The current time provided by the device clock.

    </div>

  - <div id="sdk-for-android-navigate-getDefault" class="section detail">

    ### getDefault

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-wallclock" title="interface in com.here.sdk.navigation">WallClock</a></span> <span class="element-name">getDefault</span>()

    </div>

    <div class="block">

    Provides the default WallClock implementation based on the device clock.

    </div>

    Returns:  
    The default WallClock instance that uses the device clock.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

