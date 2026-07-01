---
title: "AuthenticationCallback (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-authenticationcallback"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.core](sdk-for-android-explore-com-here-sdk-core-package-summary)

</div>

<div id="class-description" class="section class-description">

Functional Interface:  
This is a functional interface and can therefore be used as the
assignment target for a lambda expression or method reference.

<div class="type-signature">

<span class="annotations"><a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html"
class="external-link"
title="class or interface in java.lang">@FunctionalInterface</a>
</span><span class="modifiers">public interface
</span><span class="element-name type-name-label">AuthenticationCallback</span>

</div>

<div class="block">

Callback passed to Authentication.authenticate(SDKNativeEngine) . This
callback is called on the main thread asynchronously when an
authenticate call has completed.

</div>

</div>

<div class="section summary">

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Instance Methods
  Abstract Methods

  </div>

  <div id="method-summary-table.tabpanel"
  aria-labelledby="method-summary-table-tab0" role="tabpanel">

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Method</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>onTokenReceived(AuthenticationError authenticationError,
   AuthenticationData authenticationData)</code></pre></td>
  <td><div class="block">
  Callback passed to Authentication.authenticate(SDKNativeEngine) .
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

</div>

<div class="section details">

- <div id="method-detail" class="section method-details">

  - <div id="onTokenReceived(com.here.sdk.core.AuthenticationError,com.here.sdk.core.AuthenticationData)"
    class="section detail">

    ### onTokenReceived

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onTokenReceived</span><span class="parameters">(@Nullable
    [AuthenticationError](sdk-for-android-explore-com-here-sdk-core-authenticationerror "enum class in com.here.sdk.core") authenticationError,
    @Nullable
    [AuthenticationData](sdk-for-android-explore-com-here-sdk-core-authenticationdata "class in com.here.sdk.core") authenticationData)</span>

    </div>

    <div class="block">

    Callback passed to Authentication.authenticate(SDKNativeEngine) .
    This callback is called on the main thread asynchronously when an
    authenticate call has completed.

    </div>

    Parameters:  
    `authenticationError` -

    Represents the operation status. It is 'null' for an operation that
    succeeds.

    `authenticationData` -

    Represents the authentication data.

    </div>

  </div>

</div>

