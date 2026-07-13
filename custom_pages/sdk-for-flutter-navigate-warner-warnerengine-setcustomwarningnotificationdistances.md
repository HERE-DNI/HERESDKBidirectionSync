---
title: "setCustomWarningNotificationDistances method - WarnerEngine class - warner library - Dart API"
slug: "sdk-for-flutter-navigate-warner-warnerengine-setcustomwarningnotificationdistances"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setCustomWarningNotificationDistances.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="warner/WarnerEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setCustomWarningNotificationDistances</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">bool</span> <span class="name">setCustomWarningNotificationDistances</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-setCustomWarningNotificationDistances-param-customWarningType" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">customWarningType</span>, </span>
2.  <span id="sdk-for-flutter-navigate-setCustomWarningNotificationDistances-param-warningNotificationDistances" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-warningnotificationdistances-class">WarningNotificationDistances</a></span> <span class="parameter-name">warningNotificationDistances</span></span>

)

</div>

<div class="section desc markdown">

Sets the warning notification distances for the specified custom warning type.

Unlike <a href="sdk-for-flutter-navigate-warner-warnerengine-setwarningnotificationdistances">WarnerEngine.setWarningNotificationDistances</a>, which applies settings to a <a href="sdk-for-flutter-navigate-navigation-warningtype">WarningType</a>, this method allows configuring notification distances independently for each custom warning category identified by `WarnerEngine.setCustomWarningNotificationDistances.customWarningType`, as defined in <a href="sdk-for-flutter-navigate-warner-customwarning-customwarningtype">CustomWarning.customWarningType</a> and <a href="sdk-for-flutter-navigate-warner-warning-customwarningtype">Warning.customWarningType</a>.

- `customWarningType` The identifier of the custom warning type for which the notification distances should be set.

- `warningNotificationDistances` The warning notification distances to be applied for the specified `WarnerEngine.setCustomWarningNotificationDistances.customWarningType`.

Returns `bool`. True if the distances were successfully set; false otherwise.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Implementation

``` dart
bool setCustomWarningNotificationDistances(int customWarningType, WarningNotificationDistances warningNotificationDistances);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
