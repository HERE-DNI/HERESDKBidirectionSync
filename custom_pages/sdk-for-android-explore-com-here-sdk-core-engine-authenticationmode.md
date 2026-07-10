---
title: "AuthenticationMode (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-engine-authenticationmode"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-com-here-sdk-core-engine-package-summary">com.here.sdk.core.engine</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.core.engine.AuthenticationMode → com.here.NativeBase com.here.sdk.core.engine.AuthenticationMode → com.here.sdk.core.engine.AuthenticationMode

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">AuthenticationMode</span> <span class="extends-implements">extends <a href="sdk-for-android-explore-com-here-nativebase" title="class in com.here">NativeBase</a></span>

</div>

<div class="block">

This is a bearer authentication mode which adds or does not add a header ("Authorization", "Bearer \$Token") to each online request of the module the object is added to. The token (if used) can be provided or is retrieved via key/secret from a dedicated backend.

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

  `static interface `

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-core-engine-authenticationmode-accesstokenprovider" class="type-name-link" title="interface in com.here.sdk.core.engine"><code>AuthenticationMode.AccessTokenProvider</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  This lambda is used to retrieve access token in synchronous manner.

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      equals ( Object rhs)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      hashCode ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="sdk-for-android-explore-com-here-sdk-core-engine-authenticationmode" title="class in com.here.sdk.core.engine">`AuthenticationMode`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      withExternal ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Assumes the authentication is provided by the client.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="sdk-for-android-explore-com-here-sdk-core-engine-authenticationmode" title="class in com.here.sdk.core.engine">`AuthenticationMode`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      withKeySecret ( String accessKeyId, String accessKeySecret)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  SDK will authenticate with access key id access key secret to obtain authentication token.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="sdk-for-android-explore-com-here-sdk-core-engine-authenticationmode" title="class in com.here.sdk.core.engine">`AuthenticationMode`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      withToken ( String accessToken)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  SDK will pass access token as a Bearer.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="sdk-for-android-explore-com-here-sdk-core-engine-authenticationmode" title="class in com.here.sdk.core.engine">`AuthenticationMode`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      withTokenProvider ( AuthenticationMode.AccessTokenProvider tokenProvider)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  SDK will use access token provider to retrieve access token.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-method-detail" class="section method-details">

  - <div id="sdk-for-android-explore-equals-java-lang-Object" class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr></wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a> rhs)</span>

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-explore-hashCode" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-explore-withToken-java-lang-String" class="section detail">

    ### withToken

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-core-engine-authenticationmode" title="class in com.here.sdk.core.engine">AuthenticationMode</a></span> <span class="element-name">withToken</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> accessToken)</span>

    </div>

    <div class="block">

    SDK will pass access token as a Bearer.

    </div>

    Parameters:  
    `accessToken` -

    Access token

    Returns:  
    Instance of <a href="sdk-for-android-explore-com-here-sdk-core-engine-authenticationmode" title="class in com.here.sdk.core.engine">`AuthenticationMode`</a> configured to use token

    </div>

  - <div id="sdk-for-android-explore-withTokenProvider-com-here-sdk-core-engine-AuthenticationMode-AccessTokenProvider" class="section detail">

    ### withTokenProvider

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-core-engine-authenticationmode" title="class in com.here.sdk.core.engine">AuthenticationMode</a></span> <span class="element-name">withTokenProvider</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-explore-com-here-sdk-core-engine-authenticationmode-accesstokenprovider" title="interface in com.here.sdk.core.engine">AuthenticationMode.AccessTokenProvider</a> tokenProvider)</span>

    </div>

    <div class="block">

    SDK will use access token provider to retrieve access token.

    </div>

    Parameters:  
    `tokenProvider` -

    Access token provider

    Returns:  
    Instance of <a href="sdk-for-android-explore-com-here-sdk-core-engine-authenticationmode" title="class in com.here.sdk.core.engine">`AuthenticationMode`</a> configured to use token provider

    </div>

  - <div id="sdk-for-android-explore-withExternal" class="section detail">

    ### withExternal

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-core-engine-authenticationmode" title="class in com.here.sdk.core.engine">AuthenticationMode</a></span> <span class="element-name">withExternal</span>()

    </div>

    <div class="block">

    Assumes the authentication is provided by the client.

    </div>

    Returns:  
    Instance of <a href="sdk-for-android-explore-com-here-sdk-core-engine-authenticationmode" title="class in com.here.sdk.core.engine">`AuthenticationMode`</a> configured to use externally provided authentication

    </div>

  - <div id="sdk-for-android-explore-withKeySecret-java-lang-String-java-lang-String" class="section detail">

    ### withKeySecret

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-core-engine-authenticationmode" title="class in com.here.sdk.core.engine">AuthenticationMode</a></span> <span class="element-name">withKeySecret</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> accessKeyId, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> accessKeySecret)</span>

    </div>

    <div class="block">

    SDK will authenticate with access key id access key secret to obtain authentication token.

    </div>

    Parameters:  
    `accessKeyId` -

    The access key id

    `accessKeySecret` -

    The access key secret

    Returns:  
    Instance of <a href="sdk-for-android-explore-com-here-sdk-core-engine-authenticationmode" title="class in com.here.sdk.core.engine">`AuthenticationMode`</a> configured to use key ID and secret

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

