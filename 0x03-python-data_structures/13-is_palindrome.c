#include "lists.h"

/**
 * is_palindrome - function that checks if a singly linked list
 * is a palindrome or not
 *
 * @head: is a linked list argument
 *
 * Return: 1 if the linked list is palindrome and 0 if not
*/

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (palin(head, *head));
}

/**
 * palin - function to check palindrom
 *
 * @head: head list
 *
 * @end: end list
 *
 * Return: 0
*/
int palin(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (palin(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0)
}
