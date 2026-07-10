---
title: "com.here.sdk.electronichorizon (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-electronichorizon-package-summary"
---

<div class="header">

</div>

<div class="package-signature">

package <span class="element-name">com.here.sdk.electronichorizon</span>

</div>

- <div id="sdk-for-android-navigate-class-summary">

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Class

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab2">

  <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizon" title="class in com.here.sdk.electronichorizon">ElectronicHorizon</a>

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab2">

  <div class="block">

  A class containing the full set of available paths predicted for the current vehicle state.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizondataloadedstatus" title="enum class in com.here.sdk.electronichorizon">ElectronicHorizonDataLoadedStatus</a>

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab3">

  <div class="block">

  Represents the status of data that was loaded by ElectronicHorizonDataLoader .

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab2">

  <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizondataloader" title="class in com.here.sdk.electronichorizon">ElectronicHorizonDataLoader</a>

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab2">

  <div class="block">

  Loads map data for segments that belong to the ElectronicHorizonEngine paths.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizondataloadererrorcode" title="enum class in com.here.sdk.electronichorizon">ElectronicHorizonDataLoaderErrorCode</a>

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab3">

  <div class="block">

  Represents error codes that describe the result of the ElectronicHorizonDataLoader.getSegment(com.here.sdk.mapdata.DirectedOCMSegmentId) method.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab2">

  <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizondataloaderresult" title="class in com.here.sdk.electronichorizon">ElectronicHorizonDataLoaderResult</a>

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab2">

  <div class="block">

  Represents the result of a data loading operation performed by ElectronicHorizonDataLoader .

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab1">

  <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizondataloaderstatuslistener" title="interface in com.here.sdk.electronichorizon">ElectronicHorizonDataLoaderStatusListener</a>

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab1">

  <div class="block">

  Provides a listener for status updates from the ElectronicHorizonDataLoader.loadData(com.here.sdk.electronichorizon.ElectronicHorizonUpdate) method.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab2">

  <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonengine" title="class in com.here.sdk.electronichorizon">ElectronicHorizonEngine</a>

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab2">

  <div class="block">

  Provides an electronic horizon engine that continuously predicts the road network ahead of the vehicle by using detailed map data, including road topography that is currently out of sight.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonerrorcode" title="enum class in com.here.sdk.electronichorizon">ElectronicHorizonErrorCode</a>

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab3">

  <div class="block">

  Represents error codes that describe the result of the ElectronicHorizonEngine.update(com.here.sdk.navigation.MapMatchedLocation) method.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab1">

  <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonlistener" title="interface in com.here.sdk.electronichorizon">ElectronicHorizonListener</a>

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab1">

  <div class="block">

  Provides a listener for receiving updates during execution of the ElectronicHorizonEngine.update(com.here.sdk.navigation.MapMatchedLocation) method.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab2">

  <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonoptions" title="class in com.here.sdk.electronichorizon">ElectronicHorizonOptions</a>

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab2">

  <div class="block">

  Provides options to configure ElectronicHorizonEngine .

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab2">

  <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonpath" title="class in com.here.sdk.electronichorizon">ElectronicHorizonPath</a>

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab2">

  <div class="block">

  Represents a single electronic horizon path.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab2">

  <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonposition" title="class in com.here.sdk.electronichorizon">ElectronicHorizonPosition</a>

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab2">

  <div class="block">

  Provides a position on an electronic horizon path with a reference to the current item in the ElectronicHorizon .

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab2">

  <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonsegment" title="class in com.here.sdk.electronichorizon">ElectronicHorizonSegment</a>

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab2">

  <div class="block">

  Represents a segment in an ElectronicHorizonPath .

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab2">

  <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonsegmentchanges" title="class in com.here.sdk.electronichorizon">ElectronicHorizonSegmentChanges</a>

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab2">

  <div class="block">

  A class describing the set of changes in horizon segments between two consecutive updates.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab2">

  <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonsegmentid" title="class in com.here.sdk.electronichorizon">ElectronicHorizonSegmentId</a>

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab2">

  <div class="block">

  Identifies a segment in an ElectronicHorizonPath .

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab2">

  <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonupdate" title="class in com.here.sdk.electronichorizon">ElectronicHorizonUpdate</a>

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab2">

  <div class="block">

  A class representing a full update delivered via ElectronicHorizonListener notifications.

  </div>

  </div>

  </div>

  </div>

