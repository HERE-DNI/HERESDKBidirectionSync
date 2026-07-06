---
title: "Authentication (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-authentication"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.core](sdk-for-android-explore-com-here-sdk-core-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.NativeBasecom.here.sdk.core.Authentication →
com.here.NativeBase → com.here.sdk.core.Authentication

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">Authentication</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Use the authentication class to authenticate and retrieve a secure token
that can be used with other HERE services.

</div>

</div>

<div class="section summary">

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

  `static `[`AuthenticationData`](sdk-for-android-explore-com-here-sdk-core-authenticationdata "class in com.here.sdk.core")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      authenticate(SDKNativeEngine sdkNativeEngine)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Uses the authentication service that is connected to the given SDK
  engine to authenticate and retrieve a secure token.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      authenticate(SDKNativeEngine sdkNativeEngine,
       AuthenticationCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Uses the authentication service that is connected to the given SDK
  engine to authenticate and retrieve a secure token.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-authenticate(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.core.AuthenticationCallback)"
    class="section detail">

    ### authenticate

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">void</span> <span class="element-name">authenticate</span><span class="parameters">(@NonNull
    [SDKNativeEngine](sdk-for-android-explore-com-here-sdk-core-engine-sdknativeengine "class in com.here.sdk.core.engine") sdkNativeEngine,
    @NonNull
    [AuthenticationCallback](sdk-for-android-explore-com-here-sdk-core-authenticationcallback "interface in com.here.sdk.core") callback)</span>

    </div>

    <div class="block">

    Uses the authentication service that is connected to the given SDK
    engine to authenticate and retrieve a secure token. This method
    operates asynchronously.

    </div>

    Parameters:  
    `sdkNativeEngine` -

    The SDK engine instance.

    `callback` -

    Callback to retrieve an authentication token on the main thread.

    </div>

  - <div id="sdk-for-android-explore-authenticate(com.here.sdk.core.engine.SDKNativeEngine)"
    class="section detail">

    ### authenticate

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    static</span> <span class="return-type">[AuthenticationData](sdk-for-android-explore-com-here-sdk-core-authenticationdata "class in com.here.sdk.core")</span> <span class="element-name">authenticate</span><span class="parameters">(@NonNull
    [SDKNativeEngine](sdk-for-android-explore-com-here-sdk-core-engine-sdknativeengine "class in com.here.sdk.core.engine") sdkNativeEngine)</span>
    throws
    <span class="exceptions">[AuthenticationException](sdk-for-android-explore-com-here-sdk-core-authenticationexception "class in com.here.sdk.core")</span>

    </div>

    <div class="block">

    Uses the authentication service that is connected to the given SDK
    engine to authenticate and retrieve a secure token. This method
    operates synchronously.

    </div>

    Parameters:  
    `sdkNativeEngine` -

    The SDK engine instance.

    Returns:  
    Authentication data.

    Throws:  
    [`AuthenticationException`](sdk-for-android-explore-com-here-sdk-core-authenticationexception "class in com.here.sdk.core")

    Authentication exception that describes the error.

    </div>

  </div>

</div>

