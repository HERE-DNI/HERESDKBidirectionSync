---
title: "EVSearchError (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-search-evsearcherror"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.search](sdk-for-android-explore-com-here-sdk-search-package-summary)

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object java.lang.Enum \< EVSearchError \> com.here.sdk.search.EVSearchError → java.lang.Enum \< EVSearchError \> com.here.sdk.search.EVSearchError → com.here.sdk.search.EVSearchError

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

All Implemented Interfaces:  
<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" class="external-link" title="class or interface in java.io"><code>Serializable</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" class="external-link" title="class or interface in java.lang"><code>Comparable</code></a>`<`[`EVSearchError`](sdk-for-android-explore-com-here-sdk-search-evsearcherror "enum class in com.here.sdk.search")`>`, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" class="external-link" title="class or interface in java.lang.constant"><code>Constable</code></a>

<div class="type-signature">

<span class="modifiers">public enum </span><span class="element-name type-name-label">EVSearchError</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" class="external-link" title="class or interface in java.lang">Enum</a>\<[EVSearchError](sdk-for-android-explore-com-here-sdk-search-evsearcherror "enum class in com.here.sdk.search")\></span>

</div>

<div class="block">

Specifies possible errors that EVSearchEngine may report. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

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

  <a href="sdk-for-android-explore-com-here-sdk-search-evsearcherror#AUTHENTICATION_FAILED" class="member-name-link"><code>AUTHENTICATION_FAILED</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  EVCP3 operation is not authenticated.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evsearcherror#BAD_REQUEST" class="member-name-link"><code>BAD_REQUEST</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Something wrong or missing in the request.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evsearcherror#EMPTY_IDS" class="member-name-link"><code>EMPTY_IDS</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Empty list of IDs passed.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evsearcherror#EXCEEDED_USAGE_LIMIT" class="member-name-link"><code>EXCEEDED_USAGE_LIMIT</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Credentials exceeded the allowed requests limit.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evsearcherror#HTTP_ERROR" class="member-name-link"><code>HTTP_ERROR</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  A general network request error.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evsearcherror#INTERNAL_ERROR" class="member-name-link"><code>INTERNAL_ERROR</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Generic internal error.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evsearcherror#INVALID_ID" class="member-name-link"><code>INVALID_ID</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  At least one empty or invalid ID passed.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evsearcherror#NO_RESULTS_FOUND" class="member-name-link"><code>NO_RESULTS_FOUND</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  No results found.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evsearcherror#OFFLINE" class="member-name-link"><code>OFFLINE</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The device has no internet connection.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evsearcherror#OPERATION_CANCELLED" class="member-name-link"><code>OPERATION_CANCELLED</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The request was cancelled (usually by the user).

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evsearcherror#OPERATION_FAILED" class="member-name-link"><code>OPERATION_FAILED</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Search operation failed due to some reason.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evsearcherror#PARSING_ERROR" class="member-name-link"><code>PARSING_ERROR</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  EVCP3 backend returns result with unexpected json schema.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evsearcherror#PROXY_AUTHENTICATION_FAILED" class="member-name-link"><code>PROXY_AUTHENTICATION_FAILED</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Proxy is not authenticated.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evsearcherror#PROXY_SERVER_UNREACHABLE" class="member-name-link"><code>PROXY_SERVER_UNREACHABLE</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Proxy server unreachable.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evsearcherror#SERVER_UNREACHABLE" class="member-name-link"><code>SERVER_UNREACHABLE</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  EVCP3 server is unreachable.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-search-evsearcherror#TIMED_OUT" class="member-name-link"><code>TIMED_OUT</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The request timed out.

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

  `static `[`EVSearchError`](sdk-for-android-explore-com-here-sdk-search-evsearcherror "enum class in com.here.sdk.search")

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

  `static `[`EVSearchError`](sdk-for-android-explore-com-here-sdk-search-evsearcherror "enum class in com.here.sdk.search")`[]`

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

  - <div id="sdk-for-android-explore-EMPTY_IDS" class="section detail">

    ### EMPTY_IDS

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type">[EVSearchError](sdk-for-android-explore-com-here-sdk-search-evsearcherror "enum class in com.here.sdk.search")</span> <span class="element-name">EMPTY_IDS</span>

    </div>

    <div class="block">

    Empty list of IDs passed.

    </div>

    </div>

  - <div id="sdk-for-android-explore-INVALID_ID" class="section detail">

    ### INVALID_ID

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type">[EVSearchError](sdk-for-android-explore-com-here-sdk-search-evsearcherror "enum class in com.here.sdk.search")</span> <span class="element-name">INVALID_ID</span>

    </div>

    <div class="block">

    At least one empty or invalid ID passed.

    </div>

    </div>

  - <div id="sdk-for-android-explore-BAD_REQUEST" class="section detail">

    ### BAD_REQUEST

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type">[EVSearchError](sdk-for-android-explore-com-here-sdk-search-evsearcherror "enum class in com.here.sdk.search")</span> <span class="element-name">BAD_REQUEST</span>

    </div>

    <div class="block">

    Something wrong or missing in the request.

    </div>

    </div>

  - <div id="sdk-for-android-explore-PARSING_ERROR" class="section detail">

    ### PARSING_ERROR

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type">[EVSearchError](sdk-for-android-explore-com-here-sdk-search-evsearcherror "enum class in com.here.sdk.search")</span> <span class="element-name">PARSING_ERROR</span>

    </div>

    <div class="block">

    EVCP3 backend returns result with unexpected json schema.

    </div>

    </div>

  - <div id="sdk-for-android-explore-INTERNAL_ERROR" class="section detail">

    ### INTERNAL_ERROR

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type">[EVSearchError](sdk-for-android-explore-com-here-sdk-search-evsearcherror "enum class in com.here.sdk.search")</span> <span class="element-name">INTERNAL_ERROR</span>

    </div>

    <div class="block">

    Generic internal error.

    </div>

    </div>

  - <div id="sdk-for-android-explore-SERVER_UNREACHABLE" class="section detail">

    ### SERVER_UNREACHABLE

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type">[EVSearchError](sdk-for-android-explore-com-here-sdk-search-evsearcherror "enum class in com.here.sdk.search")</span> <span class="element-name">SERVER_UNREACHABLE</span>

    </div>

    <div class="block">

    EVCP3 server is unreachable.

    </div>

    </div>

  - <div id="sdk-for-android-explore-HTTP_ERROR" class="section detail">

    ### HTTP_ERROR

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type">[EVSearchError](sdk-for-android-explore-com-here-sdk-search-evsearcherror "enum class in com.here.sdk.search")</span> <span class="element-name">HTTP_ERROR</span>

    </div>

    <div class="block">

    A general network request error.

    </div>

    </div>

  - <div id="sdk-for-android-explore-AUTHENTICATION_FAILED" class="section detail">

    ### AUTHENTICATION_FAILED

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type">[EVSearchError](sdk-for-android-explore-com-here-sdk-search-evsearcherror "enum class in com.here.sdk.search")</span> <span class="element-name">AUTHENTICATION_FAILED</span>

    </div>

    <div class="block">

    EVCP3 operation is not authenticated. Check your credentials.

    </div>

    </div>

  - <div id="sdk-for-android-explore-EXCEEDED_USAGE_LIMIT" class="section detail">

    ### EXCEEDED_USAGE_LIMIT

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type">[EVSearchError](sdk-for-android-explore-com-here-sdk-search-evsearcherror "enum class in com.here.sdk.search")</span> <span class="element-name">EXCEEDED_USAGE_LIMIT</span>

    </div>

    <div class="block">

    Credentials exceeded the allowed requests limit.

    </div>

    </div>

  - <div id="sdk-for-android-explore-TIMED_OUT" class="section detail">

    ### TIMED_OUT

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type">[EVSearchError](sdk-for-android-explore-com-here-sdk-search-evsearcherror "enum class in com.here.sdk.search")</span> <span class="element-name">TIMED_OUT</span>

    </div>

    <div class="block">

    The request timed out.

    </div>

    </div>

  - <div id="sdk-for-android-explore-OFFLINE" class="section detail">

    ### OFFLINE

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type">[EVSearchError](sdk-for-android-explore-com-here-sdk-search-evsearcherror "enum class in com.here.sdk.search")</span> <span class="element-name">OFFLINE</span>

    </div>

    <div class="block">

    The device has no internet connection.

    </div>

    </div>

  - <div id="sdk-for-android-explore-OPERATION_CANCELLED" class="section detail">

    ### OPERATION_CANCELLED

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type">[EVSearchError](sdk-for-android-explore-com-here-sdk-search-evsearcherror "enum class in com.here.sdk.search")</span> <span class="element-name">OPERATION_CANCELLED</span>

    </div>

    <div class="block">

    The request was cancelled (usually by the user).

    </div>

    </div>

  - <div id="sdk-for-android-explore-PROXY_AUTHENTICATION_FAILED" class="section detail">

    ### PROXY_AUTHENTICATION_FAILED

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type">[EVSearchError](sdk-for-android-explore-com-here-sdk-search-evsearcherror "enum class in com.here.sdk.search")</span> <span class="element-name">PROXY_AUTHENTICATION_FAILED</span>

    </div>

    <div class="block">

    Proxy is not authenticated. Check your proxy credentials.

    </div>

    </div>

  - <div id="sdk-for-android-explore-PROXY_SERVER_UNREACHABLE" class="section detail">

    ### PROXY_SERVER_UNREACHABLE

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type">[EVSearchError](sdk-for-android-explore-com-here-sdk-search-evsearcherror "enum class in com.here.sdk.search")</span> <span class="element-name">PROXY_SERVER_UNREACHABLE</span>

    </div>

    <div class="block">

    Proxy server unreachable.

    </div>

    </div>

  - <div id="sdk-for-android-explore-NO_RESULTS_FOUND" class="section detail">

    ### NO_RESULTS_FOUND

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type">[EVSearchError](sdk-for-android-explore-com-here-sdk-search-evsearcherror "enum class in com.here.sdk.search")</span> <span class="element-name">NO_RESULTS_FOUND</span>

    </div>

    <div class="block">

    No results found.

    </div>

    </div>

  - <div id="sdk-for-android-explore-OPERATION_FAILED" class="section detail">

    ### OPERATION_FAILED

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type">[EVSearchError](sdk-for-android-explore-com-here-sdk-search-evsearcherror "enum class in com.here.sdk.search")</span> <span class="element-name">OPERATION_FAILED</span>

    </div>

    <div class="block">

    Search operation failed due to some reason.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail" class="section method-details">

  - <div id="sdk-for-android-explore-values" class="section detail">

    ### values

    <div class="member-signature">

    <span class="modifiers">public static</span> <span class="return-type">[EVSearchError](sdk-for-android-explore-com-here-sdk-search-evsearcherror "enum class in com.here.sdk.search")\[\]</span> <span class="element-name">values</span>()

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

    <span class="modifiers">public static</span> <span class="return-type">[EVSearchError](sdk-for-android-explore-com-here-sdk-search-evsearcherror "enum class in com.here.sdk.search")</span> <span class="element-name">valueOf</span><wbr></wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> name)</span>

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

