---
title: "TrafficFlow (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-traffic-trafficflow"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-traffic-package-summary">com.here.sdk.traffic</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.traffic.TrafficFlow → com.here.NativeBase com.here.sdk.traffic.TrafficFlow → com.here.sdk.traffic.TrafficFlow

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

All Implemented Interfaces:  
<a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficflowbase" title="interface in com.here.sdk.traffic">`TrafficFlowBase`</a>

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">TrafficFlow</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a> implements <a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficflowbase" title="interface in com.here.sdk.traffic">TrafficFlowBase</a></span>

</div>

<div class="block">

This class provides details about traffic flow along a GeoCorridor , inside a GeoCircle or a GeoBox , that represents particular path of the road network. Backends for TrafficEngine and traffic vector tiles are different however backends may share the same data. For additional information about fields, refer to Traffic API v7 API Reference: Traffic API v7 . Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getConfidence ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the confidence field value which is normalized value between 0.0 and 1.0.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `double`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getFreeFlowSpeedInMetersPerSecond ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the reference speed in meters per second along the roadway when no traffic is present.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `double`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getJamFactor ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets a value for the amount of traffic on the roadway.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Short.html" class="external-link" title="class or interface in java.lang"><code>Short</code></a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getJamTendency ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the jam tendency field value which denotes whether the congestion is increasing, decreasing, or constant.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-traffic-junctionstraversability" title="enum class in com.here.sdk.traffic">`JunctionsTraversability`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getJunctionsTraversability ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the traversability of junctions along the affected road.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficlocation" title="class in com.here.sdk.traffic">`TrafficLocation`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getLocation ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the location of the incident.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getSpeedInMetersPerSecond ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the expected speed in meters per second along the roadway; will not exceed the legal speed limit.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getSpeedUncappedInMetersPerSecond ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the expected speed in meters per second along the roadway.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-traffic-traversability" title="enum class in com.here.sdk.traffic">`Traversability`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTraversability ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the traversability of roadway.

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

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-getLocation" class="section detail">

    ### getLocation

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficlocation" title="class in com.here.sdk.traffic">TrafficLocation</a></span> <span class="element-name">getLocation</span>()

    </div>

    <div class="block">

    Gets the location of the incident.

    </div>

    Returns:  
    Defines the location affected by traffic flow.

    </div>

  - <div id="sdk-for-android-navigate-getSpeedInMetersPerSecond" class="section detail">

    ### getSpeedInMetersPerSecond

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">getSpeedInMetersPerSecond</span>()

    </div>

    <div class="block">

    Gets the expected speed in meters per second along the roadway; will not exceed the legal speed limit.

    </div>

    Returns:  
    The expected speed in meters per second along the roadway; will not exceed the legal speed limit.

    </div>

  - <div id="sdk-for-android-navigate-getSpeedUncappedInMetersPerSecond" class="section detail">

    ### getSpeedUncappedInMetersPerSecond

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">getSpeedUncappedInMetersPerSecond</span>()

    </div>

    <div class="block">

    Gets the expected speed in meters per second along the roadway. It is based on probe data (GPS coordinates sent by vehicles or mobile devices driving along that roadway). The calculated 'expected speed' may be over the legal speed limit for that roadway because people are driving over the speed limit.

    </div>

    Returns:  
    The expected speed in meters per second that a car can drive along a roadway right now; may exceed the legal speed limit.

    </div>

  - <div id="sdk-for-android-navigate-getJamTendency" class="section detail">

    ### getJamTendency

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Short.html" class="external-link" title="class or interface in java.lang">Short</a></span> <span class="element-name">getJamTendency</span>()

    </div>

    <div class="block">

    Gets the jam tendency field value which denotes whether the congestion is increasing, decreasing, or constant. The congestion tendency may take the following values: +2 - rapidly increasing congestion +1 - increasing congestion 0 - constant congestion -1 - decreasing congestion -2 - rapidly decreasing congestion Default value of 0 can be assumed when this attribute is not present.

    </div>

    Returns:  
    The jamTendency field denotes whether the congestion is increasing, decreasing, or constant.

    </div>

  - <div id="sdk-for-android-navigate-getConfidence" class="section detail">

    ### getConfidence

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">getConfidence</span>()

    </div>

    <div class="block">

    Gets the confidence field value which is normalized value between 0.0 and 1.0. It is a normalized value between 0.0 and 1.0 with the following meaning: 0.7 \< confidence \<= 1.0 indicates real time speeds 0.5 \< confidence \<= 0.7 indicates historical speeds 0.0 \< confidence \<= 0.5 indicates speed limit This field can be used to identify whether the data for a location is derived from real-time probe sources or historical information only. All confidence data 0.71 and above is based on real-time information, where a confidence value of 0.75 or greater indicates high confidence real-time information. A confidence value equal to 0.70 or lower means that the data is derived from historical data only.

    </div>

    Returns:  
    The confidence field indicates the proportion of real-time data included in the speed calculation.

    </div>

  - <div id="sdk-for-android-navigate-getTraversability" class="section detail">

    ### getTraversability

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-traversability" title="enum class in com.here.sdk.traffic">Traversability</a></span> <span class="element-name">getTraversability</span>()

    </div>

    <div class="block">

    Gets the traversability of roadway.

    </div>

    Returns:  
    The traversability of roadway.

    </div>

  - <div id="sdk-for-android-navigate-getJunctionsTraversability" class="section detail">

    ### getJunctionsTraversability

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-junctionstraversability" title="enum class in com.here.sdk.traffic">JunctionsTraversability</a></span> <span class="element-name">getJunctionsTraversability</span>()

    </div>

    <div class="block">

    Gets the traversability of junctions along the affected road.

    </div>

    Returns:  
    The traversability of junctions along the affected road.

    </div>

  - <div id="sdk-for-android-navigate-getFreeFlowSpeedInMetersPerSecond" class="section detail">

    ### getFreeFlowSpeedInMetersPerSecond

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getFreeFlowSpeedInMetersPerSecond</span>()

    </div>

    <div class="block">

    Gets the reference speed in meters per second along the roadway when no traffic is present.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficflowbase#getFreeFlowSpeedInMetersPerSecond(">`getFreeFlowSpeedInMetersPerSecond`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficflowbase" title="interface in com.here.sdk.traffic">`TrafficFlowBase`</a>

    Returns:  
    The reference speed in meters per second along the roadway when no traffic is present.

    </div>

  - <div id="sdk-for-android-navigate-getJamFactor" class="section detail">

    ### getJamFactor

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getJamFactor</span>()

    </div>

    <div class="block">

    Gets a value for the amount of traffic on the roadway. The value, between 0.0 and 10.0, indicate the expected quality of travel. A value of 0.0 indicates that there is no congestion on the roadway. As the value approaches 10.0, it indicates increasing congestion. A value of 10.0 is reserved to represent a blocked roadway (closure).

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficflowbase#getJamFactor(">`getJamFactor`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficflowbase" title="interface in com.here.sdk.traffic">`TrafficFlowBase`</a>

    Returns:  
    A value for the amount of traffic on the roadway.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

