---
title: "RoutingError (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-routingerror"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
java.lang.Enum\<RoutingError\>com.here.sdk.routing.RoutingError →
java.lang.Enum → RoutingError → com.here.sdk.routing.RoutingError

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

All Implemented Interfaces:  
<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" class="external-link" title="class or interface in java.io"><code>Serializable</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" class="external-link" title="class or interface in java.lang"><code>Comparable</code></a>`<`[`RoutingError`](sdk-for-android-explore-com-here-sdk-routing-routingerror "enum class in com.here.sdk.routing")`>`,
<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" class="external-link" title="class or interface in java.lang.constant"><code>Constable</code></a>

<div class="type-signature">

<span class="modifiers">public enum
</span><span class="element-name type-name-label">RoutingError</span>
<span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" class="external-link" title="class or interface in java.lang">Enum</a>\<[RoutingError](sdk-for-android-explore-com-here-sdk-routing-routingerror "enum class in com.here.sdk.routing")\></span>

</div>

<div class="block">

Specifies possible errors that may result from the calculation of a
route.

</div>

</div>

<div class="section summary">

- <div id="sdk-for-android-explore-nested-class-summary"
  class="section nested-class-summary">

  <div class="inherited-list">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" class="external-link" title="class or interface in java.lang"><code>Enum.EnumDesc</code></a>`<`<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" class="external-link" title="class or interface in java.lang"><code>E</code></a>` extends `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" class="external-link" title="class or interface in java.lang"><code>Enum</code></a>`<`<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" class="external-link" title="class or interface in java.lang"><code>E</code></a>`>>`

  </div>

  </div>

- <div id="sdk-for-android-explore-enum-constant-summary"
  class="section constants-summary">

  <div class="caption">

  Enum Constants

  </div>

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Enum Constant

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-routingerror#ACTIVE_MAP_UPDATE" class="member-name-link"><code>ACTIVE_MAP_UPDATE</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Route cannot be calculated due to active map update.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-routingerror#AUTHENTICATION_FAILED" class="member-name-link"><code>AUTHENTICATION_FAILED</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Routing operation is not authenticated.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-routingerror#COULD_NOT_MATCH_DESTINATION" class="member-name-link"><code>COULD_NOT_MATCH_DESTINATION</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Destination waypoint could not be matched to a road network.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-routingerror#COULD_NOT_MATCH_ORIGIN" class="member-name-link"><code>COULD_NOT_MATCH_ORIGIN</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Origin waypoint could not be matched to a road network.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-routingerror#EXCEEDED_USAGE_LIMIT" class="member-name-link"><code>EXCEEDED_USAGE_LIMIT</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Credentials exceeded the allowed requests limit.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-routingerror#FAILED_ROUTE_HANDLE_CREATION" class="member-name-link"><code>FAILED_ROUTE_HANDLE_CREATION</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  No RouteHandle was created.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-routingerror#FORBIDDEN" class="member-name-link"><code>FORBIDDEN</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The provided credentials don't give access to the requested resource.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-routingerror#HTTP_ERROR" class="member-name-link"><code>HTTP_ERROR</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  A general network request error.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-routingerror#IMPORT_FAILED" class="member-name-link"><code>IMPORT_FAILED</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  No route section was found for imported waypoints.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-routingerror#INTERNAL_ERROR" class="member-name-link"><code>INTERNAL_ERROR</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Generic internal error.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER" class="member-name-link"><code>INVALID_PARAMETER</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  An invalid input parameter.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-routingerror#NO_ISOLINE_FOUND" class="member-name-link"><code>NO_ISOLINE_FOUND</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  No isoline can be calculated for the given input.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-routingerror#NO_REACHABLE_CHARGING_STATION_FOUND" class="member-name-link"><code>NO_REACHABLE_CHARGING_STATION_FOUND</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Initial charge is not enough to reach any known charging stations.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-routingerror#NO_ROUTE_FOUND" class="member-name-link"><code>NO_ROUTE_FOUND</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  No route can be calculated for the given input.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-routingerror#NO_ROUTE_HANDLE" class="member-name-link"><code>NO_ROUTE_HANDLE</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The route has no Route.getRouteHandle() , but it was used for a
  feature that requires one.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-routingerror#OFFLINE" class="member-name-link"><code>OFFLINE</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The device has no internet connection.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-routingerror#OPERATION_CANCELLED" class="member-name-link"><code>OPERATION_CANCELLED</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Operation cancelled.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-routingerror#PARSING_ERROR" class="member-name-link"><code>PARSING_ERROR</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Error while parsing route data.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-routingerror#PROXY_AUTHENTICATION_FAILED" class="member-name-link"><code>PROXY_AUTHENTICATION_FAILED</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Proxy is not authenticated.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-routingerror#PROXY_SERVER_UNREACHABLE" class="member-name-link"><code>PROXY_SERVER_UNREACHABLE</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Proxy server unreachable.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-routingerror#ROUTE_CALCULATION_FAILED" class="member-name-link"><code>ROUTE_CALCULATION_FAILED</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Calculation did not succeed.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-routingerror#ROUTE_LENGTH_LIMIT_EXCEEDED" class="member-name-link"><code>ROUTE_LENGTH_LIMIT_EXCEEDED</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Distance between waypoints is too large for current options.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-routingerror#SERVER_UNREACHABLE" class="member-name-link"><code>SERVER_UNREACHABLE</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Routing server is unreachable.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-routingerror#TIMED_OUT" class="member-name-link"><code>TIMED_OUT</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The request timed out.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-routingerror#VIOLATED_TRANSPORT_MODE_IN_ROUTE_HANDLE_DECODING" class="member-name-link"><code>VIOLATED_TRANSPORT_MODE_IN_ROUTE_HANDLE_DECODING</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Route handle decoding failed due to forbidden segments for the
  specified transport mode.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary"
  class="section method-summary">

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

  `static `[`RoutingError`](sdk-for-android-explore-com-here-sdk-routing-routingerror "enum class in com.here.sdk.routing")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      valueOf(String name)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Returns the enum constant of this class with the specified name.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `[`RoutingError`](sdk-for-android-explore-com-here-sdk-routing-routingerror "enum class in com.here.sdk.routing")`[]`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      values()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Returns an array containing the constants of this enum class, in the
  order they are declared.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" class="external-link" title="class or interface in java.lang">Enum</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)" class="external-link" title="class or interface in java.lang"><code>compareTo</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()" class="external-link" title="class or interface in java.lang"><code>describeConstable</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()" class="external-link" title="class or interface in java.lang"><code>getDeclaringClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()" class="external-link" title="class or interface in java.lang"><code>name</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()" class="external-link" title="class or interface in java.lang"><code>ordinal</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String)" class="external-link" title="class or interface in java.lang"><code>valueOf</code></a>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">

- <div id="sdk-for-android-explore-enum-constant-detail"
  class="section constant-details">

  - <div id="sdk-for-android-explore-INTERNAL_ERROR"
    class="section detail">

    ### INTERNAL_ERROR

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[RoutingError](sdk-for-android-explore-com-here-sdk-routing-routingerror "enum class in com.here.sdk.routing")</span> <span class="element-name">INTERNAL_ERROR</span>

    </div>

    <div class="block">

    Generic internal error.

    </div>

    </div>

  - <div id="sdk-for-android-explore-INVALID_PARAMETER"
    class="section detail">

    ### INVALID_PARAMETER

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[RoutingError](sdk-for-android-explore-com-here-sdk-routing-routingerror "enum class in com.here.sdk.routing")</span> <span class="element-name">INVALID_PARAMETER</span>

    </div>

    <div class="block">

    An invalid input parameter.

    </div>

    </div>

  - <div id="sdk-for-android-explore-SERVER_UNREACHABLE"
    class="section detail">

    ### SERVER_UNREACHABLE

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[RoutingError](sdk-for-android-explore-com-here-sdk-routing-routingerror "enum class in com.here.sdk.routing")</span> <span class="element-name">SERVER_UNREACHABLE</span>

    </div>

    <div class="block">

    Routing server is unreachable.

    </div>

    </div>

  - <div id="sdk-for-android-explore-HTTP_ERROR" class="section detail">

    ### HTTP_ERROR

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[RoutingError](sdk-for-android-explore-com-here-sdk-routing-routingerror "enum class in com.here.sdk.routing")</span> <span class="element-name">HTTP_ERROR</span>

    </div>

    <div class="block">

    A general network request error.

    </div>

    </div>

  - <div id="sdk-for-android-explore-AUTHENTICATION_FAILED"
    class="section detail">

    ### AUTHENTICATION_FAILED

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[RoutingError](sdk-for-android-explore-com-here-sdk-routing-routingerror "enum class in com.here.sdk.routing")</span> <span class="element-name">AUTHENTICATION_FAILED</span>

    </div>

    <div class="block">

    Routing operation is not authenticated. Check your credentials.

    </div>

    </div>

  - <div id="sdk-for-android-explore-FORBIDDEN" class="section detail">

    ### FORBIDDEN

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[RoutingError](sdk-for-android-explore-com-here-sdk-routing-routingerror "enum class in com.here.sdk.routing")</span> <span class="element-name">FORBIDDEN</span>

    </div>

    <div class="block">

    The provided credentials don't give access to the requested
    resource.

    </div>

    </div>

  - <div id="sdk-for-android-explore-EXCEEDED_USAGE_LIMIT"
    class="section detail">

    ### EXCEEDED_USAGE_LIMIT

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[RoutingError](sdk-for-android-explore-com-here-sdk-routing-routingerror "enum class in com.here.sdk.routing")</span> <span class="element-name">EXCEEDED_USAGE_LIMIT</span>

    </div>

    <div class="block">

    Credentials exceeded the allowed requests limit.

    </div>

    </div>

  - <div id="sdk-for-android-explore-PARSING_ERROR"
    class="section detail">

    ### PARSING_ERROR

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[RoutingError](sdk-for-android-explore-com-here-sdk-routing-routingerror "enum class in com.here.sdk.routing")</span> <span class="element-name">PARSING_ERROR</span>

    </div>

    <div class="block">

    Error while parsing route data. This is not expected to happen. Try
    updating to the newest version of the SDK. If the problem persists,
    please report a bug in the SDK.

    </div>

    </div>

  - <div id="sdk-for-android-explore-NO_ROUTE_FOUND"
    class="section detail">

    ### NO_ROUTE_FOUND

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[RoutingError](sdk-for-android-explore-com-here-sdk-routing-routingerror "enum class in com.here.sdk.routing")</span> <span class="element-name">NO_ROUTE_FOUND</span>

    </div>

    <div class="block">

    No route can be calculated for the given input.

    </div>

    </div>

  - <div id="sdk-for-android-explore-TIMED_OUT" class="section detail">

    ### TIMED_OUT

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[RoutingError](sdk-for-android-explore-com-here-sdk-routing-routingerror "enum class in com.here.sdk.routing")</span> <span class="element-name">TIMED_OUT</span>

    </div>

    <div class="block">

    The request timed out.

    </div>

    </div>

  - <div id="sdk-for-android-explore-OFFLINE" class="section detail">

    ### OFFLINE

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[RoutingError](sdk-for-android-explore-com-here-sdk-routing-routingerror "enum class in com.here.sdk.routing")</span> <span class="element-name">OFFLINE</span>

    </div>

    <div class="block">

    The device has no internet connection.

    </div>

    </div>

  - <div id="sdk-for-android-explore-NO_ISOLINE_FOUND"
    class="section detail">

    ### NO_ISOLINE_FOUND

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[RoutingError](sdk-for-android-explore-com-here-sdk-routing-routingerror "enum class in com.here.sdk.routing")</span> <span class="element-name">NO_ISOLINE_FOUND</span>

    </div>

    <div class="block">

    No isoline can be calculated for the given input.

    </div>

    </div>

  - <div id="sdk-for-android-explore-NO_ROUTE_HANDLE"
    class="section detail">

    ### NO_ROUTE_HANDLE

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[RoutingError](sdk-for-android-explore-com-here-sdk-routing-routingerror "enum class in com.here.sdk.routing")</span> <span class="element-name">NO_ROUTE_HANDLE</span>

    </div>

    <div class="block">

    The route has no Route.getRouteHandle() , but it was used for a
    feature that requires one. Consider to recalculate the route with a
    route handle. See RouteOptions.enableRouteHandle .

    </div>

    </div>

  - <div id="sdk-for-android-explore-OPERATION_CANCELLED"
    class="section detail">

    ### OPERATION_CANCELLED

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[RoutingError](sdk-for-android-explore-com-here-sdk-routing-routingerror "enum class in com.here.sdk.routing")</span> <span class="element-name">OPERATION_CANCELLED</span>

    </div>

    <div class="block">

    Operation cancelled.

    </div>

    </div>

  - <div id="sdk-for-android-explore-COULD_NOT_MATCH_DESTINATION"
    class="section detail">

    ### COULD_NOT_MATCH_DESTINATION

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[RoutingError](sdk-for-android-explore-com-here-sdk-routing-routingerror "enum class in com.here.sdk.routing")</span> <span class="element-name">COULD_NOT_MATCH_DESTINATION</span>

    </div>

    <div class="block">

    Destination waypoint could not be matched to a road network. Either
    this waypoint is far from road network or not enough data has been
    downloaded. When both, origin and destination, cannot be matched,
    then the origin waypoint error will take precedence.

    </div>

    </div>

  - <div id="sdk-for-android-explore-COULD_NOT_MATCH_ORIGIN"
    class="section detail">

    ### COULD_NOT_MATCH_ORIGIN

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[RoutingError](sdk-for-android-explore-com-here-sdk-routing-routingerror "enum class in com.here.sdk.routing")</span> <span class="element-name">COULD_NOT_MATCH_ORIGIN</span>

    </div>

    <div class="block">

    Origin waypoint could not be matched to a road network. Either this
    waypoint is far from road network or not enough data has been
    downloaded. When both, origin and destination, cannot be matched,
    then the origin waypoint error will take precedence.

    </div>

    </div>

  - <div id="sdk-for-android-explore-FAILED_ROUTE_HANDLE_CREATION"
    class="section detail">

    ### FAILED_ROUTE_HANDLE_CREATION

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[RoutingError](sdk-for-android-explore-com-here-sdk-routing-routingerror "enum class in com.here.sdk.routing")</span> <span class="element-name">FAILED_ROUTE_HANDLE_CREATION</span>

    </div>

    <div class="block">

    No RouteHandle was created.

    </div>

    </div>

  - <div id="sdk-for-android-explore-IMPORT_FAILED"
    class="section detail">

    ### IMPORT_FAILED

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[RoutingError](sdk-for-android-explore-com-here-sdk-routing-routingerror "enum class in com.here.sdk.routing")</span> <span class="element-name">IMPORT_FAILED</span>

    </div>

    <div class="block">

    No route section was found for imported waypoints.

    </div>

    </div>

  - <div id="sdk-for-android-explore-NO_REACHABLE_CHARGING_STATION_FOUND"
    class="section detail">

    ### NO_REACHABLE_CHARGING_STATION_FOUND

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[RoutingError](sdk-for-android-explore-com-here-sdk-routing-routingerror "enum class in com.here.sdk.routing")</span> <span class="element-name">NO_REACHABLE_CHARGING_STATION_FOUND</span>

    </div>

    <div class="block">

    Initial charge is not enough to reach any known charging stations.

    </div>

    </div>

  - <div id="sdk-for-android-explore-ROUTE_CALCULATION_FAILED"
    class="section detail">

    ### ROUTE_CALCULATION_FAILED

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[RoutingError](sdk-for-android-explore-com-here-sdk-routing-routingerror "enum class in com.here.sdk.routing")</span> <span class="element-name">ROUTE_CALCULATION_FAILED</span>

    </div>

    <div class="block">

    Calculation did not succeed.

    </div>

    </div>

  - <div id="sdk-for-android-explore-ROUTE_LENGTH_LIMIT_EXCEEDED"
    class="section detail">

    ### ROUTE_LENGTH_LIMIT_EXCEEDED

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[RoutingError](sdk-for-android-explore-com-here-sdk-routing-routingerror "enum class in com.here.sdk.routing")</span> <span class="element-name">ROUTE_LENGTH_LIMIT_EXCEEDED</span>

    </div>

    <div class="block">

    Distance between waypoints is too large for current options.

    </div>

    </div>

  - <div id="sdk-for-android-explore-VIOLATED_TRANSPORT_MODE_IN_ROUTE_HANDLE_DECODING"
    class="section detail">

    ### VIOLATED_TRANSPORT_MODE_IN_ROUTE_HANDLE_DECODING

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[RoutingError](sdk-for-android-explore-com-here-sdk-routing-routingerror "enum class in com.here.sdk.routing")</span> <span class="element-name">VIOLATED_TRANSPORT_MODE_IN_ROUTE_HANDLE_DECODING</span>

    </div>

    <div class="block">

    Route handle decoding failed due to forbidden segments for the
    specified transport mode.

    </div>

    </div>

  - <div id="sdk-for-android-explore-PROXY_AUTHENTICATION_FAILED"
    class="section detail">

    ### PROXY_AUTHENTICATION_FAILED

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[RoutingError](sdk-for-android-explore-com-here-sdk-routing-routingerror "enum class in com.here.sdk.routing")</span> <span class="element-name">PROXY_AUTHENTICATION_FAILED</span>

    </div>

    <div class="block">

    Proxy is not authenticated. Check your proxy credentials.

    </div>

    </div>

  - <div id="sdk-for-android-explore-PROXY_SERVER_UNREACHABLE"
    class="section detail">

    ### PROXY_SERVER_UNREACHABLE

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[RoutingError](sdk-for-android-explore-com-here-sdk-routing-routingerror "enum class in com.here.sdk.routing")</span> <span class="element-name">PROXY_SERVER_UNREACHABLE</span>

    </div>

    <div class="block">

    Proxy server unreachable.

    </div>

    </div>

  - <div id="sdk-for-android-explore-ACTIVE_MAP_UPDATE"
    class="section detail">

    ### ACTIVE_MAP_UPDATE

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[RoutingError](sdk-for-android-explore-com-here-sdk-routing-routingerror "enum class in com.here.sdk.routing")</span> <span class="element-name">ACTIVE_MAP_UPDATE</span>

    </div>

    <div class="block">

    Route cannot be calculated due to active map update. Please, repeat
    the request after map update is finished successfully.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-values()" class="section detail">

    ### values

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">[RoutingError](sdk-for-android-explore-com-here-sdk-routing-routingerror "enum class in com.here.sdk.routing")\[\]</span> <span class="element-name">values</span>()

    </div>

    <div class="block">

    Returns an array containing the constants of this enum class, in the
    order they are declared.

    </div>

    Returns:  
    an array containing the constants of this enum class, in the order
    they are declared

    </div>

  - <div id="sdk-for-android-explore-valueOf(java.lang.String)"
    class="section detail">

    ### valueOf

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">[RoutingError](sdk-for-android-explore-com-here-sdk-routing-routingerror "enum class in com.here.sdk.routing")</span> <span class="element-name">valueOf</span><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> name)</span>

    </div>

    <div class="block">

    Returns the enum constant of this class with the specified name. The
    string must match exactly an identifier used to declare an enum
    constant in this class. (Extraneous whitespace characters are not
    permitted.)

    </div>

    Parameters:  
    `name` - the name of the enum constant to be returned.

    Returns:  
    the enum constant with the specified name

    Throws:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" class="external-link" title="class or interface in java.lang"><code>IllegalArgumentException</code></a> -
    if this enum class has no constant with the specified name

    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html" class="external-link" title="class or interface in java.lang"><code>NullPointerException</code></a> -
    if the argument is null

    </div>

  </div>

</div>

