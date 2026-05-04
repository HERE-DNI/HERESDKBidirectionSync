---
title: "MapContentSettings (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapcontentsettings"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapContentSettings

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.MapContentSettings
------------------------------------------------------------------------
public final class MapContentSettings extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Provides settings regarding map data which are applied globally to all map views. The settings can already be changed before a map view instance is created.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static enum `

  [MapContentSettings.TrafficRefreshPeriodErrorCode](sdk-for-android-explore-api-reference-latestmapcontentsettings-trafficrefreshperioderrorcode)

Traffic refresh period error code

`static final class `

  [MapContentSettings.TrafficRefreshPeriodException](sdk-for-android-explore-api-reference-latestmapcontentsettings-trafficrefreshperiodexception)

Traffic refresh period error exception

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static void`

  [filterTrafficIncidents](#filterTrafficIncidents(java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`TrafficIncidentType`](sdk-for-android-explore-api-reference-latesttrafficincidenttype "enum class in com.here.sdk.traffic")`> trafficIncidents)`

Filters the displayed traffic incidents so that only the ones applicable to the specified criteria are shown when general display of traffic incidents is enabled.

`static void`

  [resetTrafficIncidentFilter](#resetTrafficIncidentFilter())`()`

Removes all filters regarding Traffic Incidents so that all incidents will be displayed, when the display of Traffic Incidents is enabled using [`MapScene.enableFeatures(java.util.Map<java.lang.String, java.lang.String>)`](sdk-for-android-explore-api-reference-latestmapscene#enableFeatures(java.util.Map)) with [`MapFeatures.TRAFFIC_INCIDENTS`](sdk-for-android-explore-api-reference-latestmapfeatures#TRAFFIC_INCIDENTS).

`static void`

  [resetTrafficRefreshPeriod](#resetTrafficRefreshPeriod())`()`

Resets the traffic data (both flow and incidents) refresh period so the default traffic information validity time and the refresh period derived from the refresh period of the traffic server is used.

`static void`

  [setTrafficRefreshPeriod](#setTrafficRefreshPeriod(com.here.time.Duration))`(`[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")` value)`

Sets the traffic data refresh period for both [`MapFeatures.TRAFFIC_FLOW`](sdk-for-android-explore-api-reference-latestmapfeatures#TRAFFIC_FLOW) and [`MapFeatures.TRAFFIC_INCIDENTS`](sdk-for-android-explore-api-reference-latestmapfeatures#TRAFFIC_INCIDENTS).

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### filterTrafficIncidents

public static void filterTrafficIncidents(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[TrafficIncidentType](sdk-for-android-explore-api-reference-latesttrafficincidenttype "enum class in com.here.sdk.traffic")\> trafficIncidents)

    Filters the displayed traffic incidents so that only the ones applicable to the specified criteria are shown when general display of traffic incidents is enabled. The display of traffic incidents can be enabled using [`MapScene.enableFeatures(java.util.Map<java.lang.String, java.lang.String>)`](sdk-for-android-explore-api-reference-latestmapscene#enableFeatures(java.util.Map)) with [`MapFeatures.TRAFFIC_INCIDENTS`](sdk-for-android-explore-api-reference-latestmapfeatures#TRAFFIC_INCIDENTS).
Parameters:
    `trafficIncidents` -

    The traffic incidents to filter for, so that only applicable incidents are displayed. When the list is empty, then all traffic incidents will be displayed. If the `trafficIncidents` contains [`TrafficIncidentType.UNKNOWN`](sdk-for-android-explore-api-reference-latesttrafficincidenttype#UNKNOWN), then the traffic filter will be applied ignoring this element.

### resetTrafficIncidentFilter

public static void resetTrafficIncidentFilter()

    Removes all filters regarding Traffic Incidents so that all incidents will be displayed, when the display of Traffic Incidents is enabled using [`MapScene.enableFeatures(java.util.Map<java.lang.String, java.lang.String>)`](sdk-for-android-explore-api-reference-latestmapscene#enableFeatures(java.util.Map)) with [`MapFeatures.TRAFFIC_INCIDENTS`](sdk-for-android-explore-api-reference-latestmapfeatures#TRAFFIC_INCIDENTS).

### setTrafficRefreshPeriod

public static void setTrafficRefreshPeriod(@NonNull [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") value) throws [MapContentSettings.TrafficRefreshPeriodException](sdk-for-android-explore-api-reference-latestmapcontentsettings-trafficrefreshperiodexception "class in com.here.sdk.mapview")

    Sets the traffic data refresh period for both [`MapFeatures.TRAFFIC_FLOW`](sdk-for-android-explore-api-reference-latestmapfeatures#TRAFFIC_FLOW) and [`MapFeatures.TRAFFIC_INCIDENTS`](sdk-for-android-explore-api-reference-latestmapfeatures#TRAFFIC_INCIDENTS). By default, the traffic information validity time and the refresh period is derived from the refresh period of HERE's traffic server. The period set by this function will override the server's default setting for upcoming traffic data requests. Defaults to 60 seconds.
Parameters:
    `value` -

    Traffic data refresh period in seconds. Valid range is \[60, 300\] seconds. The shortest refresh period that can be set is 60 seconds. This means that the traffic data shown on a map view will be refreshed every minute. The longest refresh period that can be set is 300 seconds. This means that the traffic data shown on the current map view will be refreshed every 5 minutes if the viewport does not change. Note that when a viewport change occurs, new traffic data may be requested regardless of the set refresh period. For example, during turn-by-turn navigation, frequent viewport changes can result in missing traffic data, causing new requests to be made more often.

    Throws:
    [`MapContentSettings.TrafficRefreshPeriodException`](sdk-for-android-explore-api-reference-latestmapcontentsettings-trafficrefreshperiodexception "class in com.here.sdk.mapview") -

    [`MapContentSettings.TrafficRefreshPeriodException`](sdk-for-android-explore-api-reference-latestmapcontentsettings-trafficrefreshperiodexception "class in com.here.sdk.mapview") indicates what went wrong.

### resetTrafficRefreshPeriod

public static void resetTrafficRefreshPeriod()

    Resets the traffic data (both flow and incidents) refresh period so the default traffic information validity time and the refresh period derived from the refresh period of the traffic server is used.
