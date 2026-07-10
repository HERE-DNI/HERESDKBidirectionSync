---
title: "MapContentSettings (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapcontentsettings"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-com-here-sdk-mapview-package-summary">com.here.sdk.mapview</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.mapview.MapContentSettings → com.here.NativeBase com.here.sdk.mapview.MapContentSettings → com.here.sdk.mapview.MapContentSettings

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">MapContentSettings</span> <span class="extends-implements">extends <a href="sdk-for-android-explore-com-here-nativebase" title="class in com.here">NativeBase</a></span>

</div>

<div class="block">

Provides settings regarding map data which are applied globally to all map views. The settings can already be changed before a map view instance is created.

</div>

</div>

- <div id="sdk-for-android-explore-nested-class-summary" class="section nested-class-summary">

  <div class="caption">

  Nested Classes

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Class

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  `static enum `

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-mapcontentsettings-trafficrefreshperioderrorcode" class="type-name-link" title="enum class in com.here.sdk.mapview"><code>MapContentSettings.TrafficRefreshPeriodErrorCode</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Traffic refresh period error code

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final class `

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-mapcontentsettings-trafficrefreshperiodexception" class="type-name-link" title="class in com.here.sdk.mapview"><code>MapContentSettings.TrafficRefreshPeriodException</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Traffic refresh period error exception

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary" class="section method-summary">

  <div id="sdk-for-android-explore-method-summary-table">

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      filterTrafficIncidents ( List < TrafficIncidentType > trafficIncidents)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Filters the displayed traffic incidents so that only the ones applicable to the specified criteria are shown when general display of traffic incidents is enabled.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      resetTrafficIncidentFilter ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Removes all filters regarding Traffic Incidents so that all incidents will be displayed, when the display of Traffic Incidents is enabled using MapScene.enableFeatures(java.util.Map\<java.lang.String, java.lang.String\>) with MapFeatures.TRAFFIC_INCIDENTS .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      resetTrafficRefreshPeriod ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Resets the traffic data (both flow and incidents) refresh period so the default traffic information validity time and the refresh period derived from the refresh period of the traffic server is used.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      setTrafficRefreshPeriod ( Duration value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Sets the traffic data refresh period for both MapFeatures.TRAFFIC_FLOW and MapFeatures.TRAFFIC_INCIDENTS .

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-method-detail" class="section method-details">

  - <div id="sdk-for-android-explore-filterTrafficIncidents-java-util-List" class="section detail">

    ### filterTrafficIncidents

    <div class="member-signature">

    <span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">filterTrafficIncidents</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincidenttype" title="enum class in com.here.sdk.traffic">TrafficIncidentType</a>\> trafficIncidents)</span>

    </div>

    <div class="block">

    Filters the displayed traffic incidents so that only the ones applicable to the specified criteria are shown when general display of traffic incidents is enabled. The display of traffic incidents can be enabled using MapScene.enableFeatures(java.util.Map\<java.lang.String, java.lang.String\>) with MapFeatures.TRAFFIC_INCIDENTS .

    </div>

    Parameters:  
    `trafficIncidents` -

    The traffic incidents to filter for, so that only applicable incidents are displayed. When the list is empty, then all traffic incidents will be displayed. If the `trafficIncidents` contains <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficincidenttype#UNKNOWN">`TrafficIncidentType.UNKNOWN`</a>, then the traffic filter will be applied ignoring this element.

    </div>

  - <div id="sdk-for-android-explore-resetTrafficIncidentFilter" class="section detail">

    ### resetTrafficIncidentFilter

    <div class="member-signature">

    <span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">resetTrafficIncidentFilter</span>()

    </div>

    <div class="block">

    Removes all filters regarding Traffic Incidents so that all incidents will be displayed, when the display of Traffic Incidents is enabled using MapScene.enableFeatures(java.util.Map\<java.lang.String, java.lang.String\>) with MapFeatures.TRAFFIC_INCIDENTS .

    </div>

    </div>

  - <div id="sdk-for-android-explore-setTrafficRefreshPeriod-com-here-time-Duration" class="section detail">

    ### setTrafficRefreshPeriod

    <div class="member-signature">

    <span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setTrafficRefreshPeriod</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-explore-com-here-time-duration" title="class in com.here.time">Duration</a> value)</span> throws <span class="exceptions"><a href="sdk-for-android-explore-com-here-sdk-mapview-mapcontentsettings-trafficrefreshperiodexception" title="class in com.here.sdk.mapview">MapContentSettings.TrafficRefreshPeriodException</a></span>

    </div>

    <div class="block">

    Sets the traffic data refresh period for both MapFeatures.TRAFFIC_FLOW and MapFeatures.TRAFFIC_INCIDENTS . By default, the traffic information validity time and the refresh period is derived from the refresh period of HERE's traffic server. The period set by this function will override the server's default setting for upcoming traffic data requests. Defaults to 60 seconds.

    </div>

    Parameters:  
    `value` -

    Traffic data refresh period in seconds. Valid range is \[60, 300\] seconds. The shortest refresh period that can be set is 60 seconds. This means that the traffic data shown on a map view will be refreshed every minute. The longest refresh period that can be set is 300 seconds. This means that the traffic data shown on the current map view will be refreshed every 5 minutes if the viewport does not change. Note that when a viewport change occurs, new traffic data may be requested regardless of the set refresh period. For example, during turn-by-turn navigation, frequent viewport changes can result in missing traffic data, causing new requests to be made more often.

    Throws:  
    <a href="sdk-for-android-explore-com-here-sdk-mapview-mapcontentsettings-trafficrefreshperiodexception" title="class in com.here.sdk.mapview">`MapContentSettings.TrafficRefreshPeriodException`</a> -

    <a href="sdk-for-android-explore-com-here-sdk-mapview-mapcontentsettings-trafficrefreshperiodexception" title="class in com.here.sdk.mapview">`MapContentSettings.TrafficRefreshPeriodException`</a> indicates what went wrong.

    </div>

  - <div id="sdk-for-android-explore-resetTrafficRefreshPeriod" class="section detail">

    ### resetTrafficRefreshPeriod

    <div class="member-signature">

    <span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">resetTrafficRefreshPeriod</span>()

    </div>

    <div class="block">

    Resets the traffic data (both flow and incidents) refresh period so the default traffic information validity time and the refresh period derived from the refresh period of the traffic server is used.

    </div>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

