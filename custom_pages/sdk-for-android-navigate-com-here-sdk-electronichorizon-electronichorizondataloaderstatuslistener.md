---
title: "ElectronicHorizonDataLoaderStatusListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizondataloaderstatuslistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-package-summary">com.here.sdk.electronichorizon</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">ElectronicHorizonDataLoaderStatusListener</span>

</div>

<div class="block">

Provides a listener for status updates from the ElectronicHorizonDataLoader.loadData(com.here.sdk.electronichorizon.ElectronicHorizonUpdate) method. The listener receives the current state for different levels of the paths as ElectronicHorizonDataLoadedStatus . Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process. Offline availability: This property is available online and offline.

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

      onElectronicHorizonDataLoaderStatusUpdated ( Map < Integer , ElectronicHorizonDataLoadedStatus > electronicHorizonDataLoaderStatuses)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called whenever there is a change in the status of the loaded data from ElectronicHorizonDataLoader .

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onElectronicHorizonDataLoaderStatusUpdated-java-util-Map" class="section detail">

    ### onElectronicHorizonDataLoaderStatusUpdated

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onElectronicHorizonDataLoaderStatusUpdated</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" class="external-link" title="class or interface in java.util">Map</a>\<<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a>,<wbr></wbr><a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizondataloadedstatus" title="enum class in com.here.sdk.electronichorizon">ElectronicHorizonDataLoadedStatus</a>\> electronicHorizonDataLoaderStatuses)</span>

    </div>

    <div class="block">

    Called whenever there is a change in the status of the loaded data from ElectronicHorizonDataLoader .

    </div>

    Parameters:  
    `electronicHorizonDataLoaderStatuses` -

    The updated statuses of the loaded data from <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizondataloader" title="class in com.here.sdk.electronichorizon">`ElectronicHorizonDataLoader`</a>. The key is the level of a `ElectronicHorizonPath`, the value is the current status.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

