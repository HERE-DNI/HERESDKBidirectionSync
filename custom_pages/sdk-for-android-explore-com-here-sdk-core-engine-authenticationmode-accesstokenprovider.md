---
title: "AuthenticationMode.AccessTokenProvider (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-engine-authenticationmode-accesstokenprovider"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.core.engine](sdk-for-android-explore-com-here-sdk-core-engine-package-summary)

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

Enclosing class:  
[AuthenticationMode](sdk-for-android-explore-com-here-sdk-core-engine-authenticationmode "class in com.here.sdk.core.engine")

<!-- -->

Functional Interface:  
This is a functional interface and can therefore be used as the
assignment target for a lambda expression or method reference.

<div class="type-signature">

<span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" class="external-link" title="class or interface in java.lang">@FunctionalInterface</a>
</span><span class="modifiers">public static interface
</span><span class="element-name type-name-label">AuthenticationMode.AccessTokenProvider</span>

</div>

<div class="block">

This lambda is used to retrieve access token in synchronous manner. It
returns the access token or null if it is not set. The lambda is called
each time the access token is needed and it is executed on the main
thread of the application.

</div>

</div>

<div class="section summary">
<div id="sdk-for-android-explore-method-summary"
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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      apply()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  This lambda is used to retrieve access token in synchronous manner.

  </div>

  </div>

  </div>

  </div>

  </div>

</div>

<div class="section details">
<div id="sdk-for-android-explore-method-detail"
  class="section method-details">
<div id="sdk-for-android-explore-apply()" class="section detail">

    ### apply

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">apply</span>()

    </div>

    <div class="block">

    This lambda is used to retrieve access token in synchronous manner.
    It returns the access token or null if it is not set. The lambda is
    called each time the access token is needed and it is executed on
    the main thread of the application.

    </div>

    Returns:  
    Access token in case it is set or null otherwise.

    </div>

  </div>

</div>

