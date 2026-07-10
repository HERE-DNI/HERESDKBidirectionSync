---
title: "SchoolZoneWarningListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-schoolzonewarninglistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">SchoolZoneWarningListener</span>

</div>

<div class="block">

This interface should be implemented in order to receive school zone warnings.

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

      onSchoolZoneWarningUpdated ( List < SchoolZoneWarning > schoolZoneWarning)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called whenever a new school zone warning is available.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onSchoolZoneWarningUpdated-java-util-List" class="section detail">

    ### onSchoolZoneWarningUpdated

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onSchoolZoneWarningUpdated</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-navigation-schoolzonewarning" title="class in com.here.sdk.navigation">SchoolZoneWarning</a>\> schoolZoneWarning)</span>

    </div>

    <div class="block">

    Called whenever a new school zone warning is available.

    </div>

    Parameters:  
    `schoolZoneWarning` -

    The object that contains details on the school zone warning.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

