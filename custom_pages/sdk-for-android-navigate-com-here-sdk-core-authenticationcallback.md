---
title: "AuthenticationCallback (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-core-authenticationcallback"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-core-package-summary">com.here.sdk.core</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

Functional Interface:  
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

<div class="type-signature">

<span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" class="external-link" title="class or interface in java.lang">@FunctionalInterface</a> </span><span class="modifiers">public interface </span><span class="element-name type-name-label">AuthenticationCallback</span>

</div>

<div class="block">

Callback passed to Authentication.authenticate(SDKNativeEngine) . This callback is called on the main thread asynchronously when an authenticate call has completed.

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

      onTokenReceived ( AuthenticationError authenticationError, AuthenticationData authenticationData)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Callback passed to Authentication.authenticate(SDKNativeEngine) .

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onTokenReceived-com-here-sdk-core-AuthenticationError-com-here-sdk-core-AuthenticationData" class="section detail">

    ### onTokenReceived

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onTokenReceived</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-core-authenticationerror" title="enum class in com.here.sdk.core">AuthenticationError</a> authenticationError, @Nullable <a href="sdk-for-android-navigate-com-here-sdk-core-authenticationdata" title="class in com.here.sdk.core">AuthenticationData</a> authenticationData)</span>

    </div>

    <div class="block">

    Callback passed to Authentication.authenticate(SDKNativeEngine) . This callback is called on the main thread asynchronously when an authenticate call has completed.

    </div>

    Parameters:  
    `authenticationError` -

    Represents the operation status. It is 'null' for an operation that succeeds.

    `authenticationData` -

    Represents the authentication data.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

