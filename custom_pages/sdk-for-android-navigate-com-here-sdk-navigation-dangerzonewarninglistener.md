---
title: "DangerZoneWarningListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-dangerzonewarninglistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">DangerZoneWarningListener</span>

</div>

<div class="block">

This interface should be implemented in order to receive notifications about the Danger zones.

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

      onDangerZoneWarningsUpdated ( DangerZoneWarning dangerZonesWarning)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called whenever the current location has been updated.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onDangerZoneWarningsUpdated-com-here-sdk-navigation-DangerZoneWarning" class="section detail">

    ### onDangerZoneWarningsUpdated

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onDangerZoneWarningsUpdated</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-dangerzonewarning" title="class in com.here.sdk.navigation">DangerZoneWarning</a> dangerZonesWarning)</span>

    </div>

    <div class="block">

    Called whenever the current location has been updated.

    </div>

    Parameters:  
    `dangerZonesWarning` -

    The Danger zones warning.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

