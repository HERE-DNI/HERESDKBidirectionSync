---
title: "EnvironmentalZoneWarningListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-environmentalzonewarninglistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">EnvironmentalZoneWarningListener</span>

</div>

<div class="block">

This interface should be implemented in order to receive notifications about the environmental zones.

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

      onEnvironmentalZoneWarningsUpdated ( List < EnvironmentalZoneWarning > environmentalZonesWarning)

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

  - <div id="sdk-for-android-navigate-onEnvironmentalZoneWarningsUpdated-java-util-List" class="section detail">

    ### onEnvironmentalZoneWarningsUpdated

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onEnvironmentalZoneWarningsUpdated</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-navigation-environmentalzonewarning" title="class in com.here.sdk.navigation">EnvironmentalZoneWarning</a>\> environmentalZonesWarning)</span>

    </div>

    <div class="block">

    Called whenever the current location has been updated.

    </div>

    Parameters:  
    `environmentalZonesWarning` -

    The list of environmental zones.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

