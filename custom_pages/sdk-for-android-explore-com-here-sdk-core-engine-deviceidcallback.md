---
title: "DeviceIdCallback (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-engine-deviceidcallback"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.core.engine](sdk-for-android-explore-com-here-sdk-core-engine-package-summary)

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
</span><span class="element-name type-name-label">DeviceIdCallback</span>

</div>

<div class="block">

This method will be called on the main thread when
SDKNativeEngine.getDeviceId(com.here.sdk.core.engine.DeviceIdCallback)
has been completed.

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
  <td><pre><code>onDeviceIdCallbackCompleted(String deviceId)</code></pre></td>
  <td><div class="block">
  This method will be called on the main thread when
  SDKNativeEngine.getDeviceId(com.here.sdk.core.engine.DeviceIdCallback)
  has been completed.
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

  - <div id="onDeviceIdCallbackCompleted(java.lang.String)"
    class="section detail">

    ### onDeviceIdCallbackCompleted

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onDeviceIdCallbackCompleted</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> deviceId)</span>

    </div>

    <div class="block">

    This method will be called on the main thread when
    SDKNativeEngine.getDeviceId(com.here.sdk.core.engine.DeviceIdCallback)
    has been completed.

    </div>

    Parameters:  
    `deviceId` -

    Represents a deviceId, a unique identifier assigned to the device
    for this application.

    </div>

  </div>

</div>

