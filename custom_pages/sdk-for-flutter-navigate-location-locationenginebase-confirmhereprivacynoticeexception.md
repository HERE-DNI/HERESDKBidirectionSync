---
title: "confirmHEREPrivacyNoticeException method - LocationEngineBase class - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-locationenginebase-confirmhereprivacynoticeexception"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- confirmHEREPrivacyNoticeException.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/LocationEngineBase-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">confirmHEREPrivacyNoticeException</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-location-confirmationstatus">ConfirmationStatus</a></span> <span class="name">confirmHEREPrivacyNoticeException</span>(<wbr></wbr>)

</div>

<div class="section desc markdown">

By calling this method, the application developer confirms that they have received an exceptional permission from HERE in written form to **not** include a reference to the HERE Privacy Notice.

As a result, the `LocationEngine` will not collect characteristic information about the nearby mobile and Wi-Fi network signals. However, the engine will still be fully functional and it will deliver location updates when the exception can be confirmed. Note that this call should not involve user interaction and it should be executed silently by the application before starting the `LocationEngine`.

The permission for exceptional use will be verified asynchronously using your HERE SDK credentials. A missing permission will lead to stopping of the `LocationEngine` and <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.privacyNoticeUnconfirmed</a> is delivered to `LocationStatusListener`.

It is not necessary to call this method on iOS platform.

Returns <a href="sdk-for-flutter-navigate-location-confirmationstatus">ConfirmationStatus</a>. Confirmation action status. Valid values are defined in <a href="sdk-for-flutter-navigate-location-confirmationstatus">ConfirmationStatus</a>. A first-time call may result in <a href="sdk-for-flutter-navigate-location-confirmationstatus">ConfirmationStatus.pending</a>, make sure to use the `LocationStatusListener` to get notified on an unconfirmed permission.

</div>

## Implementation

``` dart
ConfirmationStatus confirmHEREPrivacyNoticeException();
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
