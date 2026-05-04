---
title: "TaskHandle (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttaskhandle"
hidden: false
---

Package [com.here.sdk.core.threading](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface TaskHandle

------------------------------------------------------------------------
public interface TaskHandle
Handle used for the manipulation of the task.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `boolean`

  [cancel](#cancel())`()`

Sets internal state of task to 'canceled'.

`boolean`

  [isCancelled](#isCancelled())`()`

Gets a boolean indicating if this task is cancelled.

`boolean`

  [isFinished](#isFinished())`()`

Gets a boolean indicating if this task is completed.

## Method Details

### cancel

boolean cancel()

    Sets internal state of task to 'canceled'. If the task is still in the queue, it will be removed from it immediately. However, if the task is in a running state, it will nevertheless be completed, as there is no way to interrupt it.
Returns:
    True, if the task was canceled. False, if the task can't be canceled due to a platform dependent reason.

### isFinished

boolean isFinished()

    Gets a boolean indicating if this task is completed.

    True, if this task is completed. Completion may be due to normal termination, an exception, or cancellation - in all of these cases, result will return `true`.
Returns:
    Completion indication.

### isCancelled

boolean isCancelled()

    Gets a boolean indicating if this task is cancelled.

    True, if this task was canceled before it completed normally.
Returns:
    Completion indication.
