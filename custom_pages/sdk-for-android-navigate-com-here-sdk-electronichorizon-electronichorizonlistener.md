---
title: "ElectronicHorizonListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonlistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-package-summary">com.here.sdk.electronichorizon</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

All Known Implementing Classes:  
<a href="sdk-for-android-navigate-com-here-sdk-warner-warnerengine" title="class in com.here.sdk.warner">`WarnerEngine`</a>

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">ElectronicHorizonListener</span>

</div>

<div class="block">

Provides a listener for receiving updates during execution of the ElectronicHorizonEngine.update(com.here.sdk.navigation.MapMatchedLocation) method. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process. Offline availability: This property is available online and offline.

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

      onElectronicHorizonUpdated ( ElectronicHorizonErrorCode errorCode, ElectronicHorizonUpdate update)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called whenever the electronic horizon subsystem produces: a new update, an error,

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onElectronicHorizonUpdated-com-here-sdk-electronichorizon-ElectronicHorizonErrorCode-com-here-sdk-electronichorizon-ElectronicHorizonUpdate" class="section detail">

    ### onElectronicHorizonUpdated

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onElectronicHorizonUpdated</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonerrorcode" title="enum class in com.here.sdk.electronichorizon">ElectronicHorizonErrorCode</a> errorCode, @Nullable <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonupdate" title="class in com.here.sdk.electronichorizon">ElectronicHorizonUpdate</a> update)</span>

    </div>

    <div class="block">

    Called whenever the electronic horizon subsystem produces: a new update, an error, The client must inspect error_code to determine whether the call represents an error or a valid update.

    </div>

    Parameters:  
    `errorCode` -

    The error associated with the horizon computation. `null` means no error.

    `update` -

    The update describing the current electronic horizon state. May be `null` if an update could not be produced. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

