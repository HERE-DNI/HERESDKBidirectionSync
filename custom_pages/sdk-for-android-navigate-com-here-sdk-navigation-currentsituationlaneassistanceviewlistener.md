---
title: "CurrentSituationLaneAssistanceViewListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-currentsituationlaneassistanceviewlistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">CurrentSituationLaneAssistanceViewListener</span>

</div>

<div class="block">

This interface should be implemented in order to receive notifications on CurrentSituationLaneAssistanceView . The current situation lane assistance view notifications describe the lane information at the current location. A new notification is evaluated with each location update. A notification is only sent when there is a change in lane data, such as a new upcoming lane. This event is supported both with a route during turn-by-turn navigation and without a route in tracking mode. During turn-by-turn navigation, the event additionally indicates which lanes help the driver stay on the route to reach the destination. However, the event does not indicate which exact lane the user is currently driving in. The listener works for offline mode as well. Note: Lane information is not available for all roads. It's mostly available for roads with painted turn directions. This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

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

      onCurrentSituationLaneAssistanceViewUpdate ( CurrentSituationLaneAssistanceView lanes)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  The callback to be called.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onCurrentSituationLaneAssistanceViewUpdate-com-here-sdk-navigation-CurrentSituationLaneAssistanceView" class="section detail">

    ### onCurrentSituationLaneAssistanceViewUpdate

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onCurrentSituationLaneAssistanceViewUpdate</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-currentsituationlaneassistanceview" title="class in com.here.sdk.navigation">CurrentSituationLaneAssistanceView</a> lanes)</span>

    </div>

    <div class="block">

    The callback to be called.

    </div>

    Parameters:  
    `lanes` -

    Lane information on the road the user is currently driving on.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

