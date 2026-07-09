---
title: "TrafficQueryError (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-com-here-sdk-traffic-package-summary">com.here.sdk.traffic</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object java.lang.Enum \< TrafficQueryError \> com.here.sdk.traffic.TrafficQueryError → java.lang.Enum \< TrafficQueryError \> com.here.sdk.traffic.TrafficQueryError → com.here.sdk.traffic.TrafficQueryError

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

All Implemented Interfaces:  
<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" class="external-link" title="class or interface in java.io"><code>Serializable</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" class="external-link" title="class or interface in java.lang"><code>Comparable</code></a>`<`<a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">`TrafficQueryError`</a>`>`, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" class="external-link" title="class or interface in java.lang.constant"><code>Constable</code></a>

<div class="type-signature">

<span class="modifiers">public enum </span><span class="element-name type-name-label">TrafficQueryError</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" class="external-link" title="class or interface in java.lang">Enum</a>\<<a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a>\></span>

</div>

<div class="block">

Represents various errors that could occur from a traffic queries. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

</div>

- <div id="sdk-for-android-explore-nested-class-summary" class="section nested-class-summary">

  <div class="inherited-list">

  ## Nested classes/interfaces inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" class="external-link" title="class or interface in java.lang">Enum</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" class="external-link" title="class or interface in java.lang"><code>Enum.EnumDesc</code></a>`<`<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" class="external-link" title="class or interface in java.lang"><code>E</code></a>` extends `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" class="external-link" title="class or interface in java.lang"><code>Enum</code></a>`<`<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" class="external-link" title="class or interface in java.lang"><code>E</code></a>`>>`

  </div>

  </div>

- <div id="sdk-for-android-explore-enum-constant-summary" class="section constants-summary">

  ## Enum Constant Summary

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

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror#AUTHENTICATION_FAILED" class="member-name-link"><code>AUTHENTICATION_FAILED</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Incident query/flow operation is not authenticated.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror#BAD_REQUEST" class="member-name-link"><code>BAD_REQUEST</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Bad request.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror#FAILED_TO_RETRIEVE_RESULT" class="member-name-link"><code>FAILED_TO_RETRIEVE_RESULT</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Failed to retrieve result since the server has returned an error or invalid result that couldn't be processed correctly.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror#FORBIDDEN" class="member-name-link"><code>FORBIDDEN</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The provided credentials don't give access to the requested resource.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror#HTTP_ERROR" class="member-name-link"><code>HTTP_ERROR</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Network request error.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror#INCIDENT_ID_NOT_FOUND" class="member-name-link"><code>INCIDENT_ID_NOT_FOUND</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Incident ID is not found in the system.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror#INTERNAL_ERROR" class="member-name-link"><code>INTERNAL_ERROR</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Internal error.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror#INVALID_FILTER_OPTIONS" class="member-name-link"><code>INVALID_FILTER_OPTIONS</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  One or several filter options are invalid.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror#INVALID_GEOMETRY" class="member-name-link"><code>INVALID_GEOMETRY</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Invalid geometry: bounding box, circle, or corridor.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror#INVALID_IN" class="member-name-link"><code>INVALID_IN</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Invalid "in" parameter: wrong type, missing or invalid "in".

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror#INVALID_INCIDENT" class="member-name-link"><code>INVALID_INCIDENT</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Invalid incident ID, type, earliestStartTime or latestEndTime.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror#INVALID_PARAMETER" class="member-name-link"><code>INVALID_PARAMETER</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  One or more input parameters in the query is not valid.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror#OFFLINE" class="member-name-link"><code>OFFLINE</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The device has no internet connection.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror#OPERATION_CANCELLED" class="member-name-link"><code>OPERATION_CANCELLED</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Operation cancelled.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror#PROXY_AUTHENTICATION_FAILED" class="member-name-link"><code>PROXY_AUTHENTICATION_FAILED</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Proxy is not authenticated.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror#PROXY_SERVER_UNREACHABLE" class="member-name-link"><code>PROXY_SERVER_UNREACHABLE</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Proxy server unreachable.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror#SERVER_UNREACHABLE" class="member-name-link"><code>SERVER_UNREACHABLE</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Server unreachable.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror#TIMED_OUT" class="member-name-link"><code>TIMED_OUT</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The request timed out.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror#TOO_MANY_REQUESTS" class="member-name-link"><code>TOO_MANY_REQUESTS</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Server has received an excessive number of requests from client within a specific timeframe and client should slow down or wait before sending more requests.

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

  `static `<a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">`TrafficQueryError`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      valueOf ( String name)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Returns the enum constant of this class with the specified name.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">`TrafficQueryError`</a>`[]`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      values ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Returns an array containing the constants of this enum class, in the order they are declared.

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

<!-- -->

- <div id="sdk-for-android-explore-enum-constant-detail" class="section constant-details">

  ## Enum Constant Details

  - <div id="sdk-for-android-explore-FAILED_TO_RETRIEVE_RESULT" class="section detail">

    ### FAILED_TO_RETRIEVE_RESULT

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></span> <span class="element-name">FAILED_TO_RETRIEVE_RESULT</span>

    </div>

    <div class="block">

    Failed to retrieve result since the server has returned an error or invalid result that couldn't be processed correctly.

    </div>

    </div>

  - <div id="sdk-for-android-explore-AUTHENTICATION_FAILED" class="section detail">

    ### AUTHENTICATION_FAILED

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></span> <span class="element-name">AUTHENTICATION_FAILED</span>

    </div>

    <div class="block">

    Incident query/flow operation is not authenticated. Check your credentials.

    </div>

    </div>

  - <div id="sdk-for-android-explore-FORBIDDEN" class="section detail">

    ### FORBIDDEN

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></span> <span class="element-name">FORBIDDEN</span>

    </div>

    <div class="block">

    The provided credentials don't give access to the requested resource.

    </div>

    </div>

  - <div id="sdk-for-android-explore-SERVER_UNREACHABLE" class="section detail">

    ### SERVER_UNREACHABLE

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></span> <span class="element-name">SERVER_UNREACHABLE</span>

    </div>

    <div class="block">

    Server unreachable.

    </div>

    </div>

  - <div id="sdk-for-android-explore-TIMED_OUT" class="section detail">

    ### TIMED_OUT

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></span> <span class="element-name">TIMED_OUT</span>

    </div>

    <div class="block">

    The request timed out.

    </div>

    </div>

  - <div id="sdk-for-android-explore-OFFLINE" class="section detail">

    ### OFFLINE

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></span> <span class="element-name">OFFLINE</span>

    </div>

    <div class="block">

    The device has no internet connection.

    </div>

    </div>

  - <div id="sdk-for-android-explore-HTTP_ERROR" class="section detail">

    ### HTTP_ERROR

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></span> <span class="element-name">HTTP_ERROR</span>

    </div>

    <div class="block">

    Network request error.

    </div>

    </div>

  - <div id="sdk-for-android-explore-INVALID_IN" class="section detail">

    ### INVALID_IN

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></span> <span class="element-name">INVALID_IN</span>

    </div>

    <div class="block">

    Invalid "in" parameter: wrong type, missing or invalid "in".

    </div>

    </div>

  - <div id="sdk-for-android-explore-INVALID_GEOMETRY" class="section detail">

    ### INVALID_GEOMETRY

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></span> <span class="element-name">INVALID_GEOMETRY</span>

    </div>

    <div class="block">

    Invalid geometry: bounding box, circle, or corridor.

    </div>

    </div>

  - <div id="sdk-for-android-explore-INVALID_INCIDENT" class="section detail">

    ### INVALID_INCIDENT

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></span> <span class="element-name">INVALID_INCIDENT</span>

    </div>

    <div class="block">

    Invalid incident ID, type, earliestStartTime or latestEndTime.

    </div>

    </div>

  - <div id="sdk-for-android-explore-INCIDENT_ID_NOT_FOUND" class="section detail">

    ### INCIDENT_ID_NOT_FOUND

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></span> <span class="element-name">INCIDENT_ID_NOT_FOUND</span>

    </div>

    <div class="block">

    Incident ID is not found in the system.

    </div>

    </div>

  - <div id="sdk-for-android-explore-INVALID_FILTER_OPTIONS" class="section detail">

    ### INVALID_FILTER_OPTIONS

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></span> <span class="element-name">INVALID_FILTER_OPTIONS</span>

    </div>

    <div class="block">

    One or several filter options are invalid.

    </div>

    </div>

  - <div id="sdk-for-android-explore-INVALID_PARAMETER" class="section detail">

    ### INVALID_PARAMETER

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></span> <span class="element-name">INVALID_PARAMETER</span>

    </div>

    <div class="block">

    One or more input parameters in the query is not valid.

    </div>

    </div>

  - <div id="sdk-for-android-explore-INTERNAL_ERROR" class="section detail">

    ### INTERNAL_ERROR

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></span> <span class="element-name">INTERNAL_ERROR</span>

    </div>

    <div class="block">

    Internal error.

    </div>

    </div>

  - <div id="sdk-for-android-explore-OPERATION_CANCELLED" class="section detail">

    ### OPERATION_CANCELLED

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></span> <span class="element-name">OPERATION_CANCELLED</span>

    </div>

    <div class="block">

    Operation cancelled.

    </div>

    </div>

  - <div id="sdk-for-android-explore-PROXY_AUTHENTICATION_FAILED" class="section detail">

    ### PROXY_AUTHENTICATION_FAILED

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></span> <span class="element-name">PROXY_AUTHENTICATION_FAILED</span>

    </div>

    <div class="block">

    Proxy is not authenticated. Check your proxy credentials.

    </div>

    </div>

  - <div id="sdk-for-android-explore-PROXY_SERVER_UNREACHABLE" class="section detail">

    ### PROXY_SERVER_UNREACHABLE

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></span> <span class="element-name">PROXY_SERVER_UNREACHABLE</span>

    </div>

    <div class="block">

    Proxy server unreachable. Error indicates a problem with a proxy server's accessibility or connectivity.

    </div>

    </div>

  - <div id="sdk-for-android-explore-BAD_REQUEST" class="section detail">

    ### BAD_REQUEST

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></span> <span class="element-name">BAD_REQUEST</span>

    </div>

    <div class="block">

    Bad request. Error indicates server could not understand or process the request made by the client because the request itself was malformed or incorrect.

    </div>

    </div>

  - <div id="sdk-for-android-explore-TOO_MANY_REQUESTS" class="section detail">

    ### TOO_MANY_REQUESTS

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></span> <span class="element-name">TOO_MANY_REQUESTS</span>

    </div>

    <div class="block">

    Server has received an excessive number of requests from client within a specific timeframe and client should slow down or wait before sending more requests.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail" class="section method-details">

  - <div id="sdk-for-android-explore-values" class="section detail">

    ### values

    <div class="member-signature">

    <span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a>\[\]</span> <span class="element-name">values</span>()

    </div>

    <div class="block">

    Returns an array containing the constants of this enum class, in the order they are declared.

    </div>

    Returns:  
    an array containing the constants of this enum class, in the order they are declared

    </div>

  - <div id="sdk-for-android-explore-valueOf-java-lang-String" class="section detail">

    ### valueOf

    <div class="member-signature">

    <span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></span> <span class="element-name">valueOf</span><wbr></wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> name)</span>

    </div>

    <div class="block">

    Returns the enum constant of this class with the specified name. The string must match exactly an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)

    </div>

    Parameters:  
    `name` - the name of the enum constant to be returned.

    Returns:  
    the enum constant with the specified name

    Throws:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" class="external-link" title="class or interface in java.lang"><code>IllegalArgumentException</code></a> - if this enum class has no constant with the specified name

    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html" class="external-link" title="class or interface in java.lang"><code>NullPointerException</code></a> - if the argument is null

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

