<?php

declare(strict_types=1);

namespace ConjoinCloud\Generated\Api;

use ConjoinCloud\CallOptions;
use ConjoinCloud\ConjoinClient;
use ConjoinCloud\HttpMethod;
use ConjoinCloud\Internal\Request\PathSegment;
use ConjoinCloud\OperationRequest;
use ConjoinCloud\Pagination\ListPage;

final class RelayPipelines
{
    public function __construct(private readonly ConjoinClient $client)
    {
    }

    public function readPipelineDefinitions(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'relay/pipelines/',
            query: $query,
        ), $options);
    }

    public function createPipelineDefinition(array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'relay/pipelines/',
            body: $data,
        ), $options)->dataArray();
    }

    public function readPipelineDefinitionsCount(?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'relay/pipelines/count',
            query: $query,
        ), $options)->dataArray();
    }

    public function updatePipelineDefinition(string $pipelineId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Patch,
            path: 'relay/pipelines/' . PathSegment::encode($pipelineId),
            body: $data,
        ), $options)->dataArray();
    }

    public function deletePipelineDefinition(string $pipelineId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Delete,
            path: 'relay/pipelines/' . PathSegment::encode($pipelineId),
        ), $options)->dataArray();
    }

    public function triggerPipelineRun(string $pipelineId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'relay/pipelines/' . PathSegment::encode($pipelineId) . '/trigger',
            body: $data,
        ), $options)->dataArray();
    }

    public function readPipelineRuns(?array $query = null, ?CallOptions $options = null): ListPage
    {
        return $this->client->sendList(new OperationRequest(
            method: HttpMethod::Get,
            path: 'relay/pipeline-runs/',
            query: $query,
        ), $options);
    }

    public function readPipelineRunsCount(?array $query = null, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'relay/pipeline-runs/count',
            query: $query,
        ), $options)->dataArray();
    }

    public function readPipelineRun(string $pipelineRunId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Get,
            path: 'relay/pipeline-runs/' . PathSegment::encode($pipelineRunId),
        ), $options)->dataArray();
    }

    public function cancelPipelineRun(string $pipelineRunId, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'relay/pipeline-runs/' . PathSegment::encode($pipelineRunId) . '/cancel',
        ), $options)->dataArray();
    }

    public function approvePipelineGate(string $pipelineRunId, string $stepId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'relay/pipeline-runs/'
                . PathSegment::encode($pipelineRunId)
                . '/steps/'
                . PathSegment::encode($stepId)
                . '/approve',
            body: $data,
        ), $options)->dataArray();
    }

    public function rejectPipelineGate(string $pipelineRunId, string $stepId, array $data, ?CallOptions $options = null): array
    {
        return $this->client->send(new OperationRequest(
            method: HttpMethod::Post,
            path: 'relay/pipeline-runs/'
                . PathSegment::encode($pipelineRunId)
                . '/steps/'
                . PathSegment::encode($stepId)
                . '/reject',
            body: $data,
        ), $options)->dataArray();
    }
}
