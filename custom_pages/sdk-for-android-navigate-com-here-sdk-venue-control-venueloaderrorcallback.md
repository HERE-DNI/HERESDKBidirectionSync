---
title: "VenueLoadErrorCallback (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-control-venueloaderrorcallback"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-venue-control-package-summary">com.here.sdk.venue.control</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

Functional Interface:  
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

<div class="type-signature">

<span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" class="external-link" title="class or interface in java.lang">@FunctionalInterface</a> </span><span class="modifiers">public interface </span><span class="element-name type-name-label">VenueLoadErrorCallback</span>

</div>

<div class="block">

A method which is called on the main thread when VenueMap.selectVenueAsync(String, VenueLoadErrorCallback) has been completed.

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

      onVenueLoadError ( VenueErrorCode error)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  A method which is called on the main thread when VenueMap.selectVenueAsync(String, VenueLoadErrorCallback) has been completed.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onVenueLoadError-com-here-sdk-venue-control-VenueErrorCode" class="section detail">

    ### onVenueLoadError

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onVenueLoadError</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venueerrorcode" title="enum class in com.here.sdk.venue.control">VenueErrorCode</a> error)</span>

    </div>

    <div class="block">

    A method which is called on the main thread when VenueMap.selectVenueAsync(String, VenueLoadErrorCallback) has been completed.

    </div>

    Parameters:  
    `error` -

    Represents an error in case of a failure. It is `null` for an operation that succeeds.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

