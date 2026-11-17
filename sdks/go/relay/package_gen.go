package relay

import conjoin "github.com/conjoin-cloud/conjoin-sdk/sdks/go"

type Client struct {
	Broadcasts   *BroadcastsService
	Events       *EventsService
	Memorystores *MemorystoresService
	Pipelines    *PipelinesService
	Queues       *QueuesService
	Schedulers   *SchedulersService
	Searches     *SearchesService
	Settings     *SettingsService
}

func New(client *conjoin.Client) *Client {
	return &Client{
		Broadcasts:   &BroadcastsService{client: client},
		Events:       &EventsService{client: client},
		Memorystores: &MemorystoresService{client: client},
		Pipelines:    &PipelinesService{client: client},
		Queues:       &QueuesService{client: client},
		Schedulers:   &SchedulersService{client: client},
		Searches:     &SearchesService{client: client},
		Settings:     &SettingsService{client: client},
	}
}
