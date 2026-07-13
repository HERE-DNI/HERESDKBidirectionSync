---
title: "confirmHEREPrivacyNoticeInclusion method - LocationEngineBase class - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-locationenginebase-confirmhereprivacynoticeinclusion"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/LocationEngineBase-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">confirmHEREPrivacyNoticeInclusion</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-location-confirmationstatus">ConfirmationStatus</a></span> <span class="name">confirmHEREPrivacyNoticeInclusion</span>(<wbr></wbr>)

</div>

<div class="section desc markdown">

It is the responsibility of the application developer to ensure that the application user is informed about the collection of characteristic information regarding nearby mobile and Wi-Fi network signals.

Additionally, a link to the related <a href="https://legal.here.com/en-gb/here-network-positioning-via-sdk">HERE Privacy Notice</a> must be made available to the user.

This information can be included in the application's Terms & Conditions, Privacy Policy, or otherwise made accessible to the user.

An example text for informing users about the data collection: "This application uses location services provided by HERE Technologies. To maintain, improve, and provide these services, HERE Technologies occasionally collects characteristic information about nearby mobile and Wi-Fi network signals. For more information, please refer to the HERE Privacy Notice at: <https://legal.here.com/en-gb/here-network-positioning-via-sdk%22>

**Note:** By calling this method, the application developer confirms that this information is made available to the end user.

For example, it is sufficient to inform users once that using the app requires acceptance of its terms (if any). Then, in the terms include the above mentioned data collection information and a link to the related HERE Privacy Notice. The user is not required to open the terms to acknowledge the data collection details. The "Positioning" example app on <a href="https://github.com/heremaps/here-sdk-examples">GitHub</a> provides an example of this.

When the above criteria are met, it is recommended to silently execute this method each time before starting the `LocationEngine`, as failure to do so will result in the engine being non-functional.

It is not necessary to call this method on the iOS platform.

Returns <a href="sdk-for-flutter-navigate-location-confirmationstatus">ConfirmationStatus</a>. Immediately returns with <a href="sdk-for-flutter-navigate-location-confirmationstatus">ConfirmationStatus.ok</a>.

</div>

## Implementation

``` dart
ConfirmationStatus confirmHEREPrivacyNoticeInclusion();
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

