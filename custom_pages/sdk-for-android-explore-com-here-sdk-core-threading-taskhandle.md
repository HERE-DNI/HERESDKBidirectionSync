---
title: "TaskHandle (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-threading-taskhandle"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.core.threading](sdk-for-android-explore-com-here-sdk-core-threading-package-summary)

</div>

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">TaskHandle</span>

</div>

<div class="block">

Handle used for the manipulation of the task.

</div>

</div>

- <div id="sdk-for-android-explore-method-summary" class="section method-summary">

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

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      cancel ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets internal state of task to 'canceled'.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `boolean`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      isCancelled ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets a boolean indicating if this task is cancelled.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      isFinished ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets a boolean indicating if this task is completed.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-method-detail" class="section method-details">

  - <div id="sdk-for-android-explore-cancel" class="section detail">

    ### cancel

    <div class="member-signature">

    <span class="return-type">boolean</span> <span class="element-name">cancel</span>()

    </div>

    <div class="block">

    Sets internal state of task to 'canceled'. If the task is still in the queue, it will be removed from it immediately. However, if the task is in a running state, it will nevertheless be completed, as there is no way to interrupt it.

    </div>

    Returns:  
    True, if the task was canceled. False, if the task can't be canceled due to a platform dependent reason.

    </div>

  - <div id="sdk-for-android-explore-isFinished" class="section detail">

    ### isFinished

    <div class="member-signature">

    <span class="return-type">boolean</span> <span class="element-name">isFinished</span>()

    </div>

    <div class="block">

    Gets a boolean indicating if this task is completed. True, if this task is completed. Completion may be due to normal termination, an exception, or cancellation - in all of these cases, result will return true .

    </div>

    Returns:  
    Completion indication.

    </div>

  - <div id="sdk-for-android-explore-isCancelled" class="section detail">

    ### isCancelled

    <div class="member-signature">

    <span class="return-type">boolean</span> <span class="element-name">isCancelled</span>()

    </div>

    <div class="block">

    Gets a boolean indicating if this task is cancelled. True, if this task was canceled before it completed normally.

    </div>

    Returns:  
    Completion indication.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

