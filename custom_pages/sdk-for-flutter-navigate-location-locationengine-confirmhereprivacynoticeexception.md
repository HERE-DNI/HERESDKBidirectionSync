---
title: "confirmHEREPrivacyNoticeException method - LocationEngine class - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-locationengine-confirmhereprivacynoticeexception"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/LocationEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">confirmHEREPrivacyNoticeException</span> method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-location-confirmationstatus">ConfirmationStatus</a></span> <span class="name">confirmHEREPrivacyNoticeException</span>(<wbr></wbr>)

<div class="features">

<span class="feature">override</span>

</div>

</div>

<div class="section desc markdown">

On Android devices by calling this method, the application developer confirms that they have received an exceptional permission from HERE in written form to **not** include a reference to the HERE Privacy Notice. As a result, the `LocationEngine` will not collect characteristic information about the nearby mobile and Wi-Fi network signals. However, the engine will still be fully functional and will deliver location updates when the exception can be confirmed.

**Note:** This call should not involve user interaction and should be executed silently by the application before starting the `LocationEngine`.

The permission for exceptional use will be verified asynchronously using your HERE SDK credentials. A missing permission will cause the `LocationEngine` to stop, and `LocationEngineStatus.PRIVACY_NOTICE_UNCONFIRMED` will be delivered to the `LocationStatusListener`.

Returns:

- A confirmation action status. Valid values are defined in <a href="sdk-for-flutter-navigate-location-confirmationstatus">ConfirmationStatus</a>.
- A first-time call may result in `ConfirmationStatus.PENDING`. Ensure that the `LocationStatusListener` is used to get notified if permission remains unconfirmed.

On iOS devices this method does nothing and <a href="sdk-for-flutter-navigate-location-confirmationstatus">ConfirmationStatus.ok</a> is returned.

</div>

## Implementation

``` dart
ConfirmationStatus confirmHEREPrivacyNoticeException() =>
    _location.confirmHEREPrivacyNoticeException();
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

